
import logging

from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

# Вставь сюда токен от @BotFather
TOKEN = "8888063193:AAGSdz-zrC3qMfsS_kTm5XmdHypIKgsYrcE"

# Локальный SOCKS5-прокси Happ
PROXY = "socks5://127.0.0.1:10808"

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logging.getLogger("httpx").setLevel(logging.WARNING)

# Кнопки меню
keyboard = [
    [
        KeyboardButton("👤 Мой профиль"),
        KeyboardButton("ℹ️ Помощь"),
    ],
    [
        KeyboardButton("⚙️ Настройки"),
        KeyboardButton("🎮 Развлечения"),
    ],
]

menu = ReplyKeyboardMarkup(
    keyboard,
    resize_keyboard=True,
    input_field_placeholder="Выбери действие...",
)


async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    await update.message.reply_text(
        "Привет! 👋\n\n"
        "Добро пожаловать в моего бота!\n"
        "Выбери действие с помощью меню ниже.",
        reply_markup=menu,
    )


async def handle_menu(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    text = update.message.text
    user = update.effective_user

    if text == "👤 Мой профиль":
        username = (
            f"@{user.username}"
            if user.username
            else "Не указан"
        )
        await update.message.reply_text(
            f"👤 Твой профиль\n\n"
            f"Имя: {user.first_name}\n"
            f"ID: {user.id}\n"
            f"Username: {username}",
            reply_markup=menu,
        )

    elif text == "ℹ️ Помощь":
        await update.message.reply_text(
            "ℹ️ Помощь\n\n"
            "Выбирай кнопки меню, чтобы пользоваться ботом.\n"
            "Команда /start открывает главное меню.",
            reply_markup=menu,
        )

    elif text == "⚙️ Настройки":
        await update.message.reply_text(
            "⚙️ Настройки\n\n"
            "Здесь мы сможем добавить настройки "
            "уведомлений, языка и другие функции.",
            reply_markup=menu,
        )

    elif text == "🎮 Развлечения":
        await update.message.reply_text(
            "🎮 Развлечения\n\n"
            "Почему Python любят программисты?\n"
            "Потому что с ним всё становится проще! 🐍",
            reply_markup=menu,
        )

    else:
        await update.message.reply_text(
            "Не знаю такой команды. Используй меню ниже.",
            reply_markup=menu,
        )


def main():
    if TOKEN == "ВСТАВЬ_СЮДА_СВОЙ_ТОКЕН":
        raise ValueError(
            "Сначала вставь токен своего бота в переменную TOKEN."
        )

    app = (
        Application.builder()
        .token(TOKEN)
        .proxy(PROXY)
        .get_updates_proxy(PROXY)
        .build()
    )

    app.add_handler(CommandHandler("start", start))
    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            handle_menu,
        )
    )

    print("Бот запускается через прокси Happ...")
    app.run_polling()


if __name__ == "__main__":
    main()
