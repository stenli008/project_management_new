from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone
from django.utils.text import slugify

from ProjectManagement.accounts.models import WorkerUser


class Client(models.Model):
    first_name = models.CharField(max_length=120, blank=False, null=False)
    last_name = models.CharField(max_length=120, blank=False, null=False)
    organisation = models.CharField(max_length=120, blank=True, null=False)
    phone_number = models.CharField(max_length=120, blank=True, null=False)
    email = models.EmailField(blank=True, null=False)
    address = models.CharField(max_length=120, blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Project(models.Model):
    project_name = models.CharField(max_length=120, blank=False, null=False, unique=True)
    address = models.CharField(max_length=120, blank=False, null=False)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, blank=False, null=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.project_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.project_name

    @property
    def get_tasks(self):
        return self.task_set.all()


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
    requirement = models.IntegerField(
        validators=[MinValueValidator(1)],
        blank=False,
        null=False,
    )
    date_added = models.DateField(auto_now_add=True)
    deadline = models.DateField(blank=False, null=False)
    complete = models.BooleanField(default=False)
    work_done = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    slug = models.SlugField(unique=False, blank=True)

    @property
    def days_left(self):
        today = timezone.now().date()
        days_left = (self.deadline - today).days
        return max(0, days_left)

    @property
    def progress(self):
        percent = (self.work_done / int(self.requirement)) * 100
        return f'{percent:.0f}'

    def __str__(self):
        return f'{self.task_category.name} in project: {self.project.project_name}'

    def save(self, *args, **kwargs):
        value = f'{self.task_category}-{self.task_category}-{self.deadline}'
        if self.requirement == self.work_done:
            self.complete = True
        self.slug = slugify(value)
        super().save(*args, **kwargs)
