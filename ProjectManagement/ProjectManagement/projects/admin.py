from django.contrib import admin

from ProjectManagement.projects.models import Project, Task, TaskCategory


class TaskCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'unit']


admin.site.register(TaskCategory, TaskCategoryAdmin)
admin.site.register(Project)
admin.site.register(Task)
