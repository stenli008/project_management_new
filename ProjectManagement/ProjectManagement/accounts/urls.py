from django.urls import path, include

from ProjectManagement.accounts.views import UserRegisterView, UserLoginView, UserLogoutView

urlpatterns = (
    path('account/', include([
        path('register/', UserRegisterView.as_view(), name='accounts-register-page'),
        path('login/', UserLoginView.as_view(), name='accounts-login-page'),
        path('logout/', UserLogoutView.as_view(), name='accounts-logout-page'),
    ])),
)