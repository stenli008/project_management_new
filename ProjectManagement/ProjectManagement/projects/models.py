from django.core.validators import MinValueValidator
from django.db import models

from ProjectManagement.accounts.models import WorkerUser


class Project(models.Model):
    project_name = models.CharField(max_length=120, blank=False, null=False)

    def __str__(self):
        return self.project_name


class TaskCategory(models.Model):
    CHOICES = (
        ('METERS', 'Meters'),
        ('NUMBER', 'Number'),
    )
    name = models.CharField(max_length=30, blank=False, null=False)
    unit = models.CharField(choices=CHOICES, max_length=100, blank=False, null=False)

    def __str__(self):
        return self.name


class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, blank=False, null=True)
    workers = models.ManyToManyField(WorkerUser, related_name='tasks')
    task_category = models.ForeignKey(TaskCategory, on_delete=models.SET_NULL, null=True, blank=False)
    quantity = models.IntegerField(
        validators=[MinValueValidator(1)],
        blank=False,
        null=False,
    )

    def __str__(self):
        return f'{self.task_category.name} in project: {self.project.project_name}'
