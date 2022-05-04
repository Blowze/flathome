/* eslint-disable no-undef */
function configureMainButton({ text, color, textColor = "#ffffff", onclick }) {
    Telegram.WebApp.MainButton.text = text.toUpperCase();
    Telegram.WebApp.MainButton.color = color;
    Telegram.WebApp.MainButton.textColor = textColor;
    Telegram.WebApp.MainButton.onClick(onclick);
}
export default configureMainButton;
