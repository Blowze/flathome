import json
from random import randint
from time import sleep

import requests
from bs4 import BeautifulSoup as bs
from requests import Session

template_url_params = "newobjects/list?deal_type=sale&engine_version=2&offer_type=newobject&region={}&p={}"


with open("settings.txt", "r", encoding="utf-8") as f:
    r = f.read().split("\n")
    for i in r:
        t = i.split(": ")
        if t[0] == "rucaptcha":
            RUCAPTCHA = t[1]


def captcha_solution(url: str) -> str:
    site_key = '6LdpqSQUAAAAAJXo9mQJY2QYw2rSi2D0-ZXctcw_'

    id = requests.post("https://rucaptcha.com/in.php", params={
        "key": RUCAPTCHA,
        "method": "userrecaptcha",
        "googlekey": site_key,
        "pageurl": url,
        "json": 1
    })

    capt_id = id.json()["request"]

    while True:
        response = requests.get("https://rucaptcha.com/res.php", params={
            "key": RUCAPTCHA,
            "action": "get",
            "id": capt_id
        })

        if response.text == 'CAPCHA_NOT_READY':
            sleep(5)
        else:
            break

    return response.text.split("|")[-1]


def get_data_item(ses: Session, url_item: str):

    resp = ses.get(url_item)
    sp = bs(resp.text, "lxml")

    script = sp.find_all("script", {"type": "text/javascript"})

    if len(script) == 1:
        captcha = captcha_solution(resp.url)

        resp = ses.post(resp.url, data={
            "g-recaptcha-response": captcha,
            "redirect_url": url_item
        })

        sp = bs(resp.text, "lxml")

        script = sp.find_all("script", {"type": "text/javascript"})

    for i in script:
        try:
            if i.string.find('''initialState''') != -1:
                script = i.string
                break
        except Exception as e:
            print(e)
            continue

    script = script.split('''] = ''')[-1][:-2]

    js = json.loads(script)

    k1 = ""
    k2 = ""
    k3 = ""
    k4 = ""
    k5 = ""
    mn = ""
    sv = ""
    st = ""
    sk1 = ""
    sk2 = ""
    sk3 = ""
    sk4 = ""
    sk5 = ""
    smn = ""
    ssv = ""
    sst = ""
    type_metro = ""

    try:
        pr = sp.find("div", {"data-name": "OffersReliableBlock"}).find("p").text
    except Exception as e:
        print(e)
        pr = ""
    t = sp.find("div", {"data-name": "LabelsLayout"}).find_all("span")
    labels = ""
    for i in t:
        if i.text in ('Надёжный ЖК', 'Эскроу'):
            continue
        #else:
        #    print(i.text)
        if labels != "":
            labels += f"#{i.text}"
        else:
            labels += i.text
    #print(labels)
    for i in js:
        if i['key'] == 'initialState':
            j = i['value']
            build_id = j['newbuilding']['id']
            name = j['newbuilding']['name']
            city = j['newbuilding']['fullAddress'].split(",")[0]
            address = j['newbuilding']['fullAddress']
            geo = f"{j['newbuilding']['geo']['coordinates']['lat']},{j['newbuilding']['geo']['coordinates']['lng']}"
            try:
                underground = j['newbuilding']['geo']['undergroundInfo'][0]['name']
            except Exception as e:
                print(e)
                underground = ""
            try:
                ot_underground = j['newbuilding']['geo']['undergroundInfo'][0]['timeWalk']
                type_metro = "пешком"
            except Exception as e:
                print(e)
                ot_underground = ""

            if ot_underground == "" or int(ot_underground) > 20:
                try:
                    ot_underground = j['newbuilding']['geo']['undergroundInfo'][0]['timeTransport']
                    type_metro = "на транспорте"
                except Exception as e:
                    print(e)
                    pass
            try:
                builder = j['newbuilding']['builders'][0]['name']
            except Exception as e:
                builder = None
                print(e)
            try:
                url_builder = j['newbuilding']['builders'][0]['website']
            except Exception as e:
                url_builder = None
                print(e)
            if url_builder is None:
                url_builder = ""
            try:
                deadline = j['newbuilding']['specialStatusDisplay']
            except Exception as e:
                deadline = ""
                print(e)
            try:
                if 'newbuildingClass' in j['newbuilding']:
                    class_ = j['newbuilding']['newbuildingClass']
                elif 'newbuildingClassName' in j['newbuilding']:
                    class_ = j['newbuilding']['newbuildingClassName']
                else:
                    class_ = ""
            except Exception as e:
                class_ = ""
                print(e)


            for t in j['newbuilding']['specifications']:
                if t['title'] == "Этажность":
                    try:
                        floor = t['value']
                    except Exception as e:
                        print(e)
                        floor = ""

            sp = bs(j['newbuilding']['description'], "lxml")
            description = sp.text.replace(";", ".")
            image = ",".join([i['fullUrl'] for i in j['newbuilding']["media"]])

            for t in j['offers']['data']['total']['fromDeveloperRooms']:
                if t['roomTypeDisplay'] == '1-комнатные':
                    k1 = t['price2Range']
                    sk1 = t['totalAreaMinDisplay']
                elif t['roomTypeDisplay'] == '2-комнатные':
                    k2 = t['price2Range']
                    sk2 = t['totalAreaMinDisplay']
                elif t['roomTypeDisplay'] == '3-комнатные':
                    k3 = t['price2Range']
                    sk3 = t['totalAreaMinDisplay']
                elif t['roomTypeDisplay'] == '4-комнатные':
                    k4 = t['price2Range']
                    sk4 = t['totalAreaMinDisplay']
                elif t['roomTypeDisplay'] == '5-комнатные':
                    k5 = t['price2Range']
                    sk5 = t['totalAreaMinDisplay']
                elif t['roomTypeDisplay'] == 'Многокомнатные':
                    mn = t['price2Range']
                    smn = t['totalAreaMinDisplay']
                elif t['roomTypeDisplay'] == 'Свободные планировки':
                    sv = t['price2Range']
                    ssv = t['totalAreaMinDisplay']
                elif t['roomTypeDisplay'] == 'Студии':
                    st = t['price2Range']
                    sst = t['totalAreaMinDisplay']

    with open(f'{filename}.csv', 'a', newline="", encoding="utf-8") as f:
        f.write(f"{build_id};{name};{city};{address};{geo};{underground};{ot_underground};{type_metro};{builder};{url_builder};{deadline};{class_};{floor};{k1};{sk1};{k2};{sk2};{k3};{sk3};{k4};{sk4};{k5};{sk5};{mn};{smn};{sv};{ssv};{st};{sst};{description};{image};{pr};{labels}\n")
    f.close()

def check_next_page(sp) -> (str, bool):
    try:
        pages = sp.find("div", {"data-name": "Pagination"}).find_all("div", {"data-name": "Container"})

        for i in range(len(pages) + 1):
            if pages[i].find("a") is None:
                try:
                    return pages[i + 1].find("a").attrs["href"]
                except Exception as e:
                    print(e)
                    return False
    except Exception as e:
        print(e)
        return False


def parser_cian(url: str, filename: str):
    count_objects = 0
    with open(f'{filename}.csv', 'w', newline="", encoding="utf-8") as f:
        f.write(f"ID ЖК;Название ЖК;Город;Адрес;ГЕО;Метро;удалённость от метро;Тип транспорта;Название застройщика;ссылка на сайт застройщика;Сдача ЖК;Класс ЖК;Этажность;1-комнатные, цена;1-комнатные, площадь;2-комнатные, цена;2-комнатные, площадь;3-комнатные, цена;3-комнатные, площадь;4-комнатные, цена;4-комнатные, площадь;5-комнатные, цена;5-комнатные, площадь;Многокомнатные, цена;Многокомнатные, площадь;Свободные планировки, цена;Свободные планировки, площадь;Студии, цена;Студии, площадь;описание;изображения;Надёжность объекта;Лейблы\n")
    next = True
    ses = requests.session()
    headers = {
        "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36'
    }
    main_url = "/".join(url.split("/")[:3])
    while next:

        ses.headers = headers
        resp = requests.get(url, headers=headers)

        if resp.text.find('Captcha - база объявлений ЦИАН') != -1:
            captcha = captcha_solution(resp.url)

            resp = ses.post(resp.url, data={
                "g-recaptcha-response": captcha,
                "redirect_url": url
            })

        sp = bs(resp.text, "lxml")
        url = check_next_page(sp)
        if not url:
            next = False
        else:
            if main_url.endswith("/"):
                main_url = main_url[:-1]
            url = main_url + url

        try:
            items = sp.find("div", {"data-name": "OffersBody"}).find_all("div", {"data-name": "GKCardComponent"})
        except Exception as e:
            print(e)
            continue

        for item in items:
            url_item = item.find("a").attrs["href"]
            t = url_item.split("/")
            if t[2] == "www.cian.ru":
                url_item = "/".join(t[:4])
            else:
                url_item = "/".join(t[:3])
            while True:
                try:
                    get_data_item(ses, url_item)
                    count_objects += 1
                    print('Спарщено ' + str(count_objects))
                    sleep(1)
                    break
                except AttributeError as ex:
                    print(ex)
                    url_item = "/".join(t[:4])
                except Exception as exc:
                    print(exc)
                    continue
            sleep(randint(1, 3))
    print('Парсинг завершён!')
    f.close()

if __name__ == '__main__':
    url = input("ссылка >>> ")
    filename = input("название файла >>> ")
    print('Начинаем парсинг')
    parser_cian(url, filename)