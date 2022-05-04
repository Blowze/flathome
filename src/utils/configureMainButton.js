/* eslint-disable no-undef */
function configureMainButton({
    text,
    color,
    textColor = "#ffffff",
    onclick,
    isVisible = false,
}) {
    Telegram.WebApp.MainButton.text = text.toUpperCase();
    Telegram.WebApp.MainButton.color = color;
    Telegram.WebApp.MainButton.textColor = textColor;
    Telegram.WebApp.MainButton.onClick(onclick);
    Telegram.WebApp.MainButton.isVisible = isVisible;
}
export default configureMainButton;
