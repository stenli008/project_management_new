from django.contrib.auth.models import AbstractUser
from django.db import models

from ProjectManagement.faqs.models import LeaveApplication


class WorkerUser(AbstractUser):
    email = models.EmailField(blank=False, null=False)
    first_name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=30, blank=False, null=False)

    @property
    def get_sick_leave(self):
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
    def assigned_tasks(self):
        return self.tasks
