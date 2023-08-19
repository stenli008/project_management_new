from django import forms

from ProjectManagement.projects.models import Task


class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['project', 'workers', 'task_category', 'requirement', 'deadline']