from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.fsm.context import FSMContext

from fsm.registration import RegistrationFSM
from fsm.user_preferences import UserPreferencesFSM
from utils.api_client import api_request
from locales.locale import get_locale

router = Router(name="onboarding")


@router.message(CommandStart())
async def start(message: Message, state: FSMContext):
    telegram_id = message.from_user.id

    response = await api_request(
        method="GET",
        path="/internal/v1/users/profile/",
        data={"telegram_id": telegram_id}
    )

    if response.status_code == 200:
        user_data = response.json()
        await state.update_data(preferred_lang=user_data.get("preferred_lang"))
        await state.set_state(UserPreferencesFSM.preferred_lang)

        strings, keyboards = get_locale((await state.get_data()).get("preferred_lang"))

        await message.answer(
            strings["welcome_back"],
            reply_markup=keyboards["main_menu"]
        )

    elif response.status_code == 204:
        await state.set_state(RegistrationFSM.choosing_language)

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


LANG_CHOICES = {
    "English": "EN",
    "Русский": "RU",
    "Polski": "PL",
    "Беларуская": "BE",
}

@router.message(RegistrationFSM.choosing_language, F.text.in_(LANG_CHOICES.keys()))
async def choose_language(message: Message, state: FSMContext):
    lang_name = message.text
    lang_code = LANG_CHOICES[lang_name]

    user = message.from_user

    payload = {
        "telegram_id": user.id,
        "full_name": user.full_name,
        "user_name": user.username,
        "preferred_lang": lang_code,
    }

    response = await api_request(
        "POST", 
        "/internal/v1/users/profile/", 
        data=payload
    )

    if response.status_code != 201:
        await message.answer("Server is overloaded 🚧🚧🚧\nTry again later")
        return 
    
    await state.set_state(UserPreferencesFSM.preferred_lang)
    await state.update_data(preferred_lang=lang_code)

    strings, keyboards = get_locale((await state.get_data()).get("preferred_lang"))

    await message.answer(
        f"{strings['lang_selected']}\n\n{strings['welcome']}",
        reply_markup=keyboards["main_menu"]
    )