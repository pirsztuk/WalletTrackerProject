from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.fsm.context import FSMContext

from fsm.preferences import PreferencesFSM
from fsm.user_preferences import UserPreferencesFSM
from utils.api_client import api_request
from utils.i18n import locale_for, command_variants


router = Router(name="preferences")


SETTINGS_WORDS = command_variants("settings_btn")
CHANGE_LANGUAGE = command_variants("change_language_btn")
BACK_WORDS = command_variants("back_btn")

@router.message(F.text.in_(SETTINGS_WORDS))
async def settings_menu(message: Message, state: FSMContext) -> None:
    await message.delete()

    strings, keyboards = await locale_for(state, message.from_user.id)

    await state.set_state(PreferencesFSM.main)

    await message.answer(
        strings["settings_title"],
        reply_markup=keyboards["settings_menu"])
    

@router.message(PreferencesFSM.main, F.text.in_(BACK_WORDS))
async def settings_menu_back(message: Message, state: FSMContext) -> None:
    await message.delete()
    await state.set_state(None) # It should stop PreferencesFSM, but save lang preferences in FSM
    strings, keyboards = await locale_for(state, message.from_user.id)
    await message.answer(
        text=strings["main_menu_title"],
        reply_markup=keyboards["main_menu"]
    )


@router.message(PreferencesFSM.main, F.text.in_(CHANGE_LANGUAGE))
async def settings_change_language(message: Message, state: FSMContext) -> None:
    await message.delete()
    await state.set_state(PreferencesFSM.change_language)
    strings, keyboards = await locale_for(state, message.from_user.id)

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
        strings["choose_lang"],
        reply_markup=lang_kb
    )


LANG_CHOICES = {
    "English": "EN",
    "Русский": "RU",
    "Polski": "PL",
    "Беларуская": "BE",
}

@router.message(PreferencesFSM.change_language, F.text.in_(LANG_CHOICES.keys()))
async def choose_language(message: Message, state: FSMContext) -> None:
    await message.delete()

    lang_name = message.text
    lang_code = LANG_CHOICES[lang_name]

    user = message.from_user

    payload = {
        "telegram_id": user.id,
        "preferred_lang": lang_code,
    }

    response = await api_request(
        "PATCH", 
        "/internal/v1/users/profile/", 
        data=payload
    )

    if response.status_code != 200:
        await message.answer("Server is overloaded 🚧🚧🚧\nTry again later")
        return 
    
    await state.set_state(UserPreferencesFSM.preferred_lang)
    await state.update_data(preferred_lang=lang_code)

    strings, keyboards = await locale_for(state, message.from_user.id)

    await state.set_state(PreferencesFSM.main)

    await message.answer(
        f"{strings['lang_selected']}\n\n{strings['settings_title']}",
        reply_markup=keyboards["settings_menu"]
    )
