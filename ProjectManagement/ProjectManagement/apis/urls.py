from django.urls import path

from ProjectManagement.apis import views

urlpatterns = (
    path('workers/', views.ListWorkerUsersView.as_view(), name='list-workers'),
    path('workers/<int:pk>/toggle-activation/', views.UpdateWorkerUserStatus.as_view(), name='toggle-worker-status'),

)