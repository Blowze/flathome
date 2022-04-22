<template>
    <div class="welcome">
        <div class="form">
            <div class="form__input">
                <input
                    v-model="message"
                    type="text"
                    class="input"
                    placeholder="Поиск города"
                />
                <i class="input__icon icon-search"></i>
            </div>
        </div>
        <div class="form__body">
            <div class="item">
                <div class="avatar">
                    <img
                        src="https://i.pinimg.com/originals/e8/97/68/e89768eb0617f7befeb48736bce12671.png"
                        alt=""
                    />
                </div>
                <div class="info">
                    <div class="title">Москва</div>
                    <div class="status">13 Новостроек</div>
                </div>
            </div>
             <div class="item">
                <div class="avatar">
                    <img
                        src="https://newsnn.ru/attachments/5850fe322b2c98f3e28e68bd9f9a38ee56c4b3e1/store/fill/1200/630/a7ef409a429eafd92ccf7cdee2984ea77263693c0af3bebc9007cf0b5aad/a7ef409a429eafd92ccf7cdee2984ea77263693c0af3bebc9007cf0b5aad.jpg"
                        alt=""
                    />
                </div>
                <div class="info">
                    <div class="title">Нижний Новгород</div>
                    <div class="status">126 Новостроек</div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "HomeView",
    data() {
        return {
            message: "",
        };
    },
    computed: {
        // геттер вычисляемого значения
        userName() {
            // `this` указывает на экземпляр vm
            return window.Telegram.WebApp.initDataUnsafe.user;
        },
    },
    mounted() {
        window.Telegram.WebApp.MainButton.setParams({
            text: "Выбрать город",
            is_active: true,
            is_visible: true,
        });
    },

    methods: {
        getWindowWidth() {
            return window.Telegram.WebApp.expand();
        },
    },
};
</script>
<style lang="scss" scoped>
.title {
    font-weight: bold;
    color: var(--tg-theme-text-color);
    line-height: 27px;
}
.status {
    font-size: 14px;
    color: var(--tg-theme-hint-color);
}
.item {
    padding: 9px;
    border-radius: 0.75rem;
    display: flex;
    align-items: center;
    text-align: left;
    cursor: pointer;
    transition: all 0.15s ease;
    &:hover {
        background: var(--item-hover-bg);
    }
}
.avatar {
    width: 54px;
    height: 54px;
    border-radius: 50%;
    background: #ccc;
    margin-right: 16px;
    overflow: hidden;
    img {
        width: 100%;
        object-fit: cover;
        height: 100%;
    }
}
.form {
    margin-bottom: 16px;
    &__input {
        position: relative;
        color: rgba(var(--color-text-secondary-rgb), 0.5);
        display: flex;
        align-items: center;
    }
    &__icon {
    }
}
.input {
    width: 100%;
    border-radius: 50%;
    height: 2.5rem;
    border-radius: 1.25rem;
    background: var(--color-background);
    border: 2px solid var(--color-background);
    outline: none;
    transition: border-color 0.15s ease;
    color: rgba(var(--tg-theme-hint-color-rgb), 0.5);
    padding-left: 40px;
    &:focus,
    &:active {
        border-color: var(--tg-theme-link-color);
        caret-color: var(--tg-theme-link-color);
        color: var(--tg-theme-text-color);
        & + [class^="icon-"],
        & + [class*=" icon-"] {
            color: var(--tg-theme-link-color);
        }
    }
    &__icon {
        position: absolute;
        left: 16px;
        font-size: 16px;
        pointer-events: none;
    }
}
.welcome {
    width: 100%;
    max-width: 480px;
    margin: 0 auto;
    padding: 4px 16px;
    text-align: center;
    margin: auto;
}
</style>
