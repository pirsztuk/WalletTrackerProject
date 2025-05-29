from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton


router = Router(name="onboarding")




async def user_exists(user_id: int) -> bool:
    # TODO: реализовать проверку в БД
    return False

@router.message(CommandStart())
async def start(message: Message):
    user_id = message.from_user.id

    if await user_exists(user_id):

        main_kb = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="➕ Add Transaction"),
                 KeyboardButton(text="📊 Summary")],
                [KeyboardButton(text="💰 Wallets"),
                 KeyboardButton(text="⚙️ Settings")],
            ],
            resize_keyboard=True,
            one_time_keyboard=False
        )
        await message.answer(
            "Welcome back! What would you like to do today?",
            reply_markup=main_kb
        )
    else:

        lang_kb = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="English"),
                 KeyboardButton(text="Русский")],
                [KeyboardButton(text="Polski"),
                 KeyboardButton(text="Беларуская")],
            ],
            resize_keyboard=True,
            one_time_keyboard=True
        )
        await message.answer(
            "👋 Welcome to Wallet Tracker!\n\n"
            "Please select your language / Пожалуйста, выберите язык:",
            reply_markup=lang_kb
        )