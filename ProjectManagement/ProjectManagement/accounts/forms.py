from django.forms.widgets import TextInput, PasswordInput, EmailInput
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.forms import forms

from ProjectManagement.accounts.models import WorkerUser


class WorkerUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = WorkerUser
        fields = ['username', 'email', 'first_name', 'last_name']


class WorkerUserLoginForm(AuthenticationForm):
    pass
