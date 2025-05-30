from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

strings = {
    "welcome": "You're all set! Use the menu below to start tracking your finances 💸",
    "welcome_back": "Welcome back! What would you like to do today?",
    "lang_selected": "✅ Language set to English.",
}

keyboards = {
    "main_menu": ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="➕ Add Transaction"), KeyboardButton(text="📊 Summary")],
            [KeyboardButton(text="💰 Wallets"), KeyboardButton(text="⚙️ Settings")],
        ],
        resize_keyboard=True,
    )
}