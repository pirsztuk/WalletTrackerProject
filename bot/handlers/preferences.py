from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.fsm.context import FSMContext

from fsm.registration import RegistrationFSM
from fsm.user_preferences import UserPreferencesFSM
from utils.api_client import api_request
from utils.i18n import locale_for, command_variants


router = Router(name="preferences")


SETTINGS_WORDS = command_variants("settings_btn")

@router.message(F.text.in_(SETTINGS_WORDS))
async def settings_menu(message: Message, state: FSMContext) -> None:

    strings, keyboards = await locale_for(state, message.from_user.id)

    await message.answer(
        strings["settings_title"],
        reply_markup=keyboards["settings_menu"])
