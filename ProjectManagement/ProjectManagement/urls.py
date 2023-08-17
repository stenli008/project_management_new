
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ProjectManagement.projects.urls')),
    path('accounts/', include('ProjectManagement.accounts.urls')),
    path('faqs/', include('ProjectManagement.faqs.urls')),
    path('apis/', include('ProjectManagement.apis.urls')),
]
