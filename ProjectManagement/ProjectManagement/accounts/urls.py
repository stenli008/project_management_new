from django.urls import path, include

from ProjectManagement.accounts.views import UserRegisterView

urlpatterns = (
    path('accounts/', include([
        path('register/', UserRegisterView.as_view(), name='accounts-register-page'),
    ])),
)