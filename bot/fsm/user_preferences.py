from aiogram.fsm.state import StatesGroup, State

class UserPreferencesFSM(StatesGroup):
    preferred_lang = State()