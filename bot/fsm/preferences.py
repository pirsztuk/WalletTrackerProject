from aiogram.fsm.state import StatesGroup, State

class PreferencesFSM(StatesGroup):
    main = State()
    change_language = State()