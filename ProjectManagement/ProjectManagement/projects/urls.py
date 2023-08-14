from django.urls import path, include

from ProjectManagement.projects import views

urlpatterns = (
    path('', views.projects_landing_page_view, name='projects-landing-page'),
    path('faqs/', include([
        path('', views.projects_faqs_page_view, name='projects-faq-page'),
        path('leave_requests/', views.leave_requests_page_view, name='leave-request-page'),
    ]))
)