from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from ProjectManagement.accounts.forms import WorkerUserCreationForm
from ProjectManagement.accounts.models import WorkerUser


class UserRegisterView(generic.CreateView):
    model = WorkerUser
    form_class = WorkerUserCreationForm
    template_name = 'accounts/accounts-register-page.html'
    success_url = reverse_lazy('projects-landing-page-view')
