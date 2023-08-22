from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify

from ProjectManagement.faqs.models import LeaveApplication


class WorkerUser(AbstractUser):
    email = models.EmailField(blank=False, null=False)
    first_name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=30, blank=False, null=False)
    slug = models.SlugField(unique=False, blank=True)

    @property
    def get_leave(self):
        days = {
            'Unpaid': 0,
            'Paid': 0,
            'Sick': 0,
            'Total': 0,
        }
        leave_requests = LeaveApplication.objects.filter(worker=self)
        for request in leave_requests:
            days['Total'] += request.days_requested
            if request.leave_type == 'UNPAID_LEAVE':
                days['Unpaid'] += request.days_requested
            elif request.leave_type == 'PAID_LEAVE':
                days['Paid'] += request.days_requested
            else:
                days['Sick'] += request.days_requested
        return days

    @property
    def get_leave_all(self):
        leave_requests = LeaveApplication.objects.filter(worker=self)
        return leave_requests

    def save(self, *args, **kwargs):
        slug_value = f'{self.first_name}-{self.last_name}'
        self.slug = slugify(slug_value)
        super(WorkerUser, self).save(*args, **kwargs)


