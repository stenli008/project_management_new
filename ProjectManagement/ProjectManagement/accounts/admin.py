from django.contrib import admin

from ProjectManagement.accounts.models import WorkerUser


class WorkerUserAdmin(admin.ModelAdmin):
    list_display = ('username',)


admin.site.register(WorkerUser, WorkerUserAdmin)
