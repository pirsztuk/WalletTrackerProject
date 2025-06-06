from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

strings = {
    "welcome": "Усё гатова! Скарыстайся меню ніжэй, каб адсочваць свае фінансы 💸",
    "welcome_back": "Сардэчна запрашаем назад! Што жадаеце зрабіць?",
    "choose_lang": "Выберыце мову:",
    "lang_selected": "✅ Мова зменена на Беларускую.",

    "main_menu_title": "🏠 Галоўнае меню",
    "settings_title": "⚙️ Налады",
}

keyboards = {
    "main_menu": ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="➕ Дадаць транзакцыю"), KeyboardButton(text="📊 Зводка")],
            [KeyboardButton(text="💰 Кашалькі"), KeyboardButton(text="⚙️ Налады")],
        ],
        resize_keyboard=True,
    ),


    "settings_menu": ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🌐 Змяніць мову")],
            [KeyboardButton(text="⬅️ Назад")],
        ],
        resize_keyboard=True,
    )
}