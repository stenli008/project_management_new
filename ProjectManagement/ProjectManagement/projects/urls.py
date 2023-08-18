from django.urls import path, include

from ProjectManagement.projects import views

urlpatterns = (
    path('', views.projects_landing_page_view, name='projects-landing-page'),
    path('staff/', views.projects_staff_page_view, name='project-staff-page'),
)