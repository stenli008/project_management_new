from django import forms
from django.forms import DateInput

from ProjectManagement.accounts.models import WorkerUser
from ProjectManagement.projects.models import Task, Project, Client


class CreateProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_name', 'address', 'client']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['client'].widget = forms.Select(choices=Client.objects.all().values_list('id', 'full_name'))


class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['project', 'task_category', 'requirement', 'deadline']
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class EditTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['project', 'task_category', 'requirement', 'work_done', 'deadline', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
