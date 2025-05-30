from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

strings = {
    "welcome": "Усё гатова! Скарыстайся меню ніжэй, каб адсочваць свае фінансы 💸",
    "welcome_back": "Сардэчна запрашаем назад! Што жадаеце зрабіць?",
    "lang_selected": "✅ Мова змененая на Беларуская.",
}

keyboards = {
    "main_menu": ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="➕ Дадаць транзакцыю"), KeyboardButton(text="📊 Зводка")],
            [KeyboardButton(text="💰 Кашалькі"), KeyboardButton(text="⚙️ Налады")],
        ],
        resize_keyboard=True,
    )
}