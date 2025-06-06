from django import forms

LANG_CHOICES = [
    ('EN', 'English'),
    ('RU', 'Русский'),
    ('PL', 'Polski'),
    ('BE', 'Беларуская'),
]

class GetUserForm(forms.Form):
    telegram_id = forms.IntegerField(required=True)


class CreateUserForm(forms.Form):
    telegram_id = forms.IntegerField(required=True)

    full_name = forms.CharField(max_length=128, required=True)
    user_name = forms.CharField(max_length=128, required=False, empty_value=None)

    preferred_lang = forms.ChoiceField(choices=LANG_CHOICES, required=True)


class UpdateUserForm(forms.Form):
    telegram_id = forms.IntegerField(required=True)

    full_name = forms.CharField(required=False, empty_value=None)
    user_name = forms.CharField(required=False, empty_value=None)
    
    preferred_lang = forms.CharField(required=False, empty_value=None)