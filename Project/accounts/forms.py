from django import forms

from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import authenticate, get_user_model
from django.core.validators import RegexValidator
from django.db.models import Q

from django.contrib.auth import get_user_model



User = get_user_model()


class UserLoginForm(forms.Form):
    user = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean_user(self):
        return self.cleaned_data.get("user")


    def clean_password(self):
        return self.cleaned_data.get("password")
