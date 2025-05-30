from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

strings = {
    "welcome": "Wszystko gotowe! Użyj menu poniżej, aby śledzić swoje finanse 💸",
    "welcome_back": "Witamy ponownie! Co chcesz teraz zrobić?",
    "lang_selected": "✅ Język ustawiony na Polski.",
}

keyboards = {
    "main_menu": ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="➕ Dodaj transakcję"), KeyboardButton(text="📊 Podsumowanie")],
            [KeyboardButton(text="💰 Portfele"), KeyboardButton(text="⚙️ Ustawienia")],
        ],
        resize_keyboard=True,
    )
}