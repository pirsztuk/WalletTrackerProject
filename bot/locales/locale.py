from . import _en, _ru, _pl, _be

_LOCALES = {
    "EN": (_en.strings, _en.keyboards),
    "RU": (_ru.strings, _ru.keyboards),
    "PL": (_pl.strings, _pl.keyboards),
    "BE": (_be.strings, _be.keyboards),
}

def get_locale(lang_code: str):
    return _LOCALES.get(lang_code.upper())


_COMMANDS = {
    "settings_btn": {
        "EN": "⚙️ Settings",
        "RU": "⚙️ Настройки",
        "PL": "⚙️ Ustawienia",
        "BE": "⚙️ Налады",
    },

    "change_language_btn": {
        "EN": "🌐 Change language",
        "RU": "🌐 Сменить язык",
        "PL": "🌐 Zmień język",
        "BE": "🌐 Змяніць мову"
    },

    "back_btn": {
        "EN": "⬅️ Back",
        "RU": "⬅️ Назад",
        "PL": "⬅️ Wstecz",
        "BE": "⬅️ Назад"
    },

}