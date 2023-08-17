from django.contrib import admin

from ProjectManagement.accounts.models import WorkerUser


class WorkerUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'display_assigned_tasks')

    def display_assigned_tasks(self, obj):
        assigned_task_categories = [str(task.task_category) for task in obj.assigned_tasks.all()]
        return ', '.join(assigned_task_categories)

    display_assigned_tasks.short_description = 'Assigned Tasks'


admin.site.register(WorkerUser, WorkerUserAdmin)
