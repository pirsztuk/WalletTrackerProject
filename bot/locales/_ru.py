from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

strings = {
    "welcome": "Все готово! Используй меню ниже для управления финансами 💸",
    "welcome_back": "С возвращением! Что вы хотите сделать?",
    "lang_selected": "✅ Язык изменён на Русский.",

    "settings_title": "⚙️ Настройки",
}

keyboards = {
    "main_menu": ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="➕ Добавить транзакцию"), KeyboardButton(text="📊 Сводка")],
            [KeyboardButton(text="💰 Кошельки"), KeyboardButton(text="⚙️ Настройки")],
        ],
        resize_keyboard=True,
    ),


    "settings_menu": ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🌐 Сменить язык")],
            [KeyboardButton(text="⬅️ Назад")],
        ],
        resize_keyboard=True,
    )
}