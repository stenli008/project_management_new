from django.urls import path

from ProjectManagement.projects import views

urlpatterns = (
    path('', views.projects_landing_page_view, name='projects-landing-page-view'),
)