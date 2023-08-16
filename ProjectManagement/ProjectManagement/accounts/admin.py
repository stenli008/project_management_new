from django.contrib import admin

from ProjectManagement.accounts.models import WorkerUser


class WorkerUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'display_assigned_tasks')

    def display_assigned_tasks(self, obj):
        return ', '.join([task.task_name for task in obj.assigned_tasks.all()])  # Custom method to display assigned tasks

    display_assigned_tasks.short_description = 'Assigned Tasks'  # Set the column header name


admin.site.register(WorkerUser, WorkerUserAdmin)
