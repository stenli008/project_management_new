from django.urls import path, include

from ProjectManagement.projects import views

urlpatterns = (
    path('', views.projects_landing_page_view, name='projects-landing-page'),
    path('staff/', views.projects_staff_page_view, name='project-staff-page'),
    path('projects/', include([
        path('', views.projects_projects_page_view, name='projects-projects-page'),
        path('<slug:slug>/', views.projects_project_page_view, name='projects-project-page'),
        path('<slug:slug>/create-task/', views.projects_new_task_page_view, name='projects-new-task-page'),
    ])),
    path('manage-task/<slug:slug>', views.projects_task_manage_page_view, name='projects-task-manage-page'),
    path('create-project/', views.projects_new_project_page_view, name='projects-new-project-page'),
    path('worker-tasks/<slug:slug>', views.projects_worker_tasks_page_view, name='projects-worker-tasks-page'),
)
