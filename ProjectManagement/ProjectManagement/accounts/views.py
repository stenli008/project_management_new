from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import views as auth_view

from ProjectManagement.accounts.forms import WorkerUserCreationForm, WorkerUserLoginForm
from ProjectManagement.accounts.models import WorkerUser


class UserRegisterView(generic.CreateView):
    model = WorkerUser
    form_class = WorkerUserCreationForm
    template_name = 'accounts/accounts-register-page.html'
    success_url = reverse_lazy('projects-landing-page')


class UserLoginView(auth_view.LoginView):
    form_class = WorkerUserLoginForm
    template_name = 'accounts/accounts-login-page.html'
    next_page = reverse_lazy('projects-landing-page')



class UserLogoutView(auth_view.LogoutView):
    next_page = reverse_lazy('accounts-login-page')
