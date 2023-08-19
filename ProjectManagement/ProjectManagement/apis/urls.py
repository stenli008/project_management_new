from django.urls import path, include

from ProjectManagement.apis import views

urlpatterns = (
    path('workers/', views.ListWorkerUsersView.as_view(), name='list-workers'),
    path('workers/<int:pk>/toggle-activation/', views.UpdateWorkerUserStatus.as_view(), name='toggle-worker-status'),
    path('tasks/', include([
        path('', views.TaskAPIView.as_view(), name='list-tasks'),
        path('delete/<int:pk>', views.DeleteTaskView.as_view(), name='delete-task'),
    ])),

)
