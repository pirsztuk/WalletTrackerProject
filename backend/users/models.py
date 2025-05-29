from django.db import models

# Create your models here.


class User(models.Model):
    PREFERRED_LANGS = [
        ("EN", "English"),
        ("BE", "Belarusian"),
        ("PL", "Polish"),
        ("RU", "Russian"),
    ]

    telegram_id = models.BigIntegerField(unique=True)
    full_name = models.CharField(max_length=128)
    user_name = models.CharField(max_length=128, null=True)

    preferred_lang = models.CharField(max_length=2, choices=PREFERRED_LANGS, default="EN")