from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import KeyboardButton, Message, ReplyKeyboardMarkup

from fsm.registration import RegistrationFSM
from fsm.user_preferences import UserPreferencesFSM
from utils.api_client import api_request
from utils.i18n import locale_for, command_variants

router = Router(name="onboarding")


@router.message(CommandStart())
async def start(message: Message, state: FSMContext) -> None:
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

        strings, keyboards = await locale_for(state, message.from_user.id)

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
    await message.delete()


LANG_CHOICES = {
    "English": "EN",
    "Русский": "RU",
    "Polski": "PL",
    "Беларуская": "BE",
}

@router.message(RegistrationFSM.choosing_language, F.text.in_(LANG_CHOICES.keys()))
async def choose_language(message: Message, state: FSMContext) -> None:
    await message.delete()

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

    strings, keyboards = await locale_for(state, message.from_user.id)

    await message.answer(
        f"{strings['lang_selected']}\n\n{strings['welcome']}",
        reply_markup=keyboards["main_menu"]
    )