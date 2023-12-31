from django.db import models

from django.core.exceptions import ValidationError




class LeaveApplication(models.Model):
    CHOICES = (
        ('SICK_LEAVE', 'Sick Leave'),
        ('PAID_LEAVE', 'Paid Leave'),
        ('UNPAID_LEAVE', 'Unpaid Leave'),
    )

    CHOICES_STATUS = (
        ('PENDING', 'Pending'),
        ('CONFIRMED', 'Confirmed'),
        ('DECLINED', 'Declined'),
    )

    worker = models.ForeignKey('accounts.WorkerUser', on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)
    reason = models.TextField(max_length=300, blank=False, null=False)
    start_date = models.DateField(blank=False, null=False)
    end_date = models.DateField(blank=False, null=False)
    days_requested = models.PositiveIntegerField(blank=True, null=True)
    leave_type = models.CharField(max_length=30, choices=CHOICES, default='UNPAID_LEAVE', blank=False, null=False)
    status = models.CharField(max_length=30, choices=CHOICES_STATUS, default='PENDING', blank=False, null=False)

    def save(self, *args, **kwargs):
        if self.start_date > self.end_date:
            raise ValidationError('Start date must be before end date!')

        self.days_requested = (self.end_date - self.start_date).days + 1

        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.worker.get_full_name()} requests {self.days_requested} days of {self.leave_type}'


class OtherApplication(models.Model):
    worker = models.ForeignKey('accounts.WorkerUser', on_delete=models.SET_NULL, null=True)
    request_type = models.CharField(max_length=30, blank=False, null=False)
    request_description = models.TextField(max_length=300, blank=False, null=False)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.worker.get_full_name()} requests {self.request_type}'


