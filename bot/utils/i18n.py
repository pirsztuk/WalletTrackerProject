"""
Ход действий:
1) Сначала смотрит preferred_lang в FSM-state
2) Если там None — тянет язык с backend-сервера по telegram_id
3) Кеширует язык обратно в FSM, чтобы больше не ходить на сервер
4) Возвращает (strings, keyboards)
"""

from typing import Tuple, List

from aiogram.fsm.context import FSMContext
from aiogram import types

from locales.locale import get_locale, _COMMANDS
from utils.api_client import api_request


async def locale_for(
    state: FSMContext,
    tg_id: int | None = None,
) -> Tuple[dict, dict]:
    """
    Возвращает strings и keyboards для конкретного пользователя.
    """

    data = await state.get_data()
    lang = data.get("preferred_lang")

    if lang is None:
        tg_id = tg_id or data.get("telegram_id")
        if tg_id is None:
            raise ValueError("telegram_id not provided and not found in state")

        response = await api_request(
            method="GET",
            path="/internal/v1/users/profile/",
            data={"telegram_id": tg_id},
        )

        if response.status_code == 200:
            user_data = response.json()
            lang = user_data.get("preferred_lang")
            await state.update_data(preferred_lang=lang)
        else:
            lang = "EN"

    strings, keyboards = get_locale(lang)
    return strings, keyboards


def command_variants(cmd_key: str) -> List[str]:
    """
    Вернёт список всех языковых вариантов «служебной» команды.
    Удобно передавать в F.text.in_(...) или in_{}.
    """
    return list(_COMMANDS.get(cmd_key, {}).values())