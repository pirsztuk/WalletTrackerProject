from aiogram.fsm.state import StatesGroup, State

class RegistrationFSM(StatesGroup):
    choosing_language = State()