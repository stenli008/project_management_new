from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone

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
    date_added = models.DateField(auto_now_add=True)
    deadline = models.DateField(blank=False, null=False)
    complete = models.BooleanField(default=False)
    progress = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])

    @property
    def days_left(self):
        today = timezone.now().date()
        days_left = (self.deadline - today).days
        return max(0, days_left)

    def __str__(self):
        return f'{self.task_category.name} in project: {self.project.project_name}'

    def save(self, *args, **kwargs):
        if self.progress == 100:
            self.complete = True

        super().save(*args, **kwargs)
