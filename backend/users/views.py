from functools import partial
from rest_framework.views import APIView
from . import forms
from . import models
from . import serializers
from utils.http import ResponseShortcutsMixin
from utils.auth import user_token_required, service_token_required



class ServiceUserView(ResponseShortcutsMixin, APIView):
    """
    GET   /internal/v1/users/profile/  - проверка существования пользователя, получение его преференций по языку.
    POST  /internal/v1/users/profile/  — регистрация нового пользователя, вызов доступен только сервисам.
    """
    @service_token_required
    def get(self, request, *args, **kwargs):

        form = forms.GetUserForm(request.data)
        
        if not form.is_valid():
            return self.bad_request(form.errors)
        
        if not models.User.objects.filter(telegram_id=form.cleaned_data["telegram_id"]).exists():
            return self.no_content()
        
        user = models.User.objects.get(telegram_id=form.cleaned_data["telegram_id"])
        serialized = serializers.UserSerializer(user).data

        return self.ok(serialized)
    

    @service_token_required
    def post(self, request, *args, **kwargs):

        form = forms.CreateUserForm(request.data)

        if not form.is_valid():
            return self.bad_request(form.errors)
        
        
        if models.User.objects.filter(telegram_id=form.cleaned_data["telegram_id"]).exists():
            return self.bad_request("telegram_id is already taken")
        
        models.User.objects.create(
            telegram_id = form.cleaned_data["telegram_id"],
            full_name = form.cleaned_data["full_name"],
            user_name = form.cleaned_data["user_name"],
            preferred_lang = form.cleaned_data["preferred_lang"],
        )

        return self.created({"status": "ok"})
    

    @service_token_required
    def patch(self, request, *args, **kwargs):

        form = forms.UpdateUserForm(request.data)

        if not form.is_valid():
            return self.bad_request(form.errors)

        try:
            user = models.User.objects.get(telegram_id=form.cleaned_data["telegram_id"])
        except models.User.DoesNotExist:
            return self.bad_request("User not found")

        for field in ["full_name", "user_name", "preferred_lang"]:
            value = form.cleaned_data.get(field)
            if value is not None:
                setattr(user, field, value)

        user.save()

        return self.ok({"status": "updated"})