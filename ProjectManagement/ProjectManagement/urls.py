
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ProjectManagement.projects.urls')),
    path('accounts/', include('ProjectManagement.accounts.urls')),
]
