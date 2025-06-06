from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

strings = {
    "welcome": "Wszystko gotowe! Użyj menu poniżej, aby śledzić swoje finanse 💸",
    "welcome_back": "Witamy ponownie! Co chcesz teraz zrobić?",
    "choose_lang": "Wybierz język:",
    "lang_selected": "✅ Język ustawiony na Polski.",

    "main_menu_title": "🏠 Główne menu",
    "settings_title": "⚙️ Ustawienia",
}

keyboards = {
    "main_menu": ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="➕ Dodaj transakcję"), KeyboardButton(text="📊 Podsumowanie")],
            [KeyboardButton(text="💰 Portfele"), KeyboardButton(text="⚙️ Ustawienia")],
        ],
        resize_keyboard=True,
    ),


    "settings_menu": ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🌐 Zmień język")],
            [KeyboardButton(text="⬅️ Wstecz")],
        ],
        resize_keyboard=True,
    )
}