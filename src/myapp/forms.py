from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import file_upload

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password1", "password2"]


class file_uploadForm(forms.ModelForm):
    class Meta:
        model = file_upload
        fields = ("file", "file_name")
