from django import forms

LANG_CHOICES = [
    ('EN', 'English'),
    ('RU', 'Русский'),
    ('PL', 'Polski'),
    ('BE', 'Беларуская'),
]

class GetUserForm(forms.Form):

    telegram_id = forms.IntegerField()

class CreateUserForm(forms.Form):

    telegram_id = forms.IntegerField()

    full_name = forms.CharField(max_length=128)
    user_name = forms.CharField(max_length=128, required=False, empty_value=None)

    preferred_lang = forms.ChoiceField(choices=LANG_CHOICES)