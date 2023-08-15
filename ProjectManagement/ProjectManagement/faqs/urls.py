from django.urls import path

from ProjectManagement.faqs.views import faqs_page_view, leave_requests_page_view, other_requests_page_view

urlpatterns = (
    path('', faqs_page_view, name='faqs-page'),
    path('leave_request/', leave_requests_page_view, name='leave-requests-page'),
    path('other_request/', other_requests_page_view, name='other-requests-page'),

)