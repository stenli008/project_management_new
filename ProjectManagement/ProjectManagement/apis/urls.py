from django.urls import path

from ProjectManagement.apis import views

urlpatterns = (
    path('workers/', views.ListWorkerUsersView.as_view()),

)