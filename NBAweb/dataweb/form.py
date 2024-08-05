from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import *


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=25)
    password = forms.CharField(label='Password', max_length=30, widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField(label='Username', max_length=25)
    password = forms.CharField(label='Password', max_length=30, widget=forms.PasswordInput)
    password_retype = forms.CharField(label='Input Password again', max_length=30, widget=forms.PasswordInput)
    invitation_code = forms.CharField(label="Invitation Code", max_length=30)

    def clean_username(self, *args):
        username = self.cleaned_data["username"]
        if User.objects.filter(username=username).exists():
            self.add_error("username", "user exists")
        return username

    def clean_invitation_code(self):
        code = self.cleaned_data["invitation_code"]
        code_model = InvitationCode.objects.filter(code=code).first()
        if not code_model:
            return "user"
        else:
            return code_model.role

    def clean(self):
        data = self.cleaned_data
        if data["password"] != data["password_retype"]:
            self.add_error("password", "The two passwords don't match")
