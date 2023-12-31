from django.contrib import admin

from ProjectManagement.projects.models import Project, Task, TaskCategory, Client


class TaskCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'unit']


class TaskAdmin(admin.ModelAdmin):
    list_display = ['project', 'task_category', 'requirement', 'days_left', 'deadline', 'complete']


admin.site.register(TaskCategory, TaskCategoryAdmin)
admin.site.register(Project)
admin.site.register(Task, TaskAdmin)
admin.site.register(Client)
