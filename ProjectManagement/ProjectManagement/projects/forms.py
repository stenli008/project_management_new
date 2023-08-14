from django import forms

from ProjectManagement.projects.models import LeaveApplication


class LeaveApplicationForm(forms.ModelForm):
    class Meta:
        model = LeaveApplication
        fields = {'start_date', 'end_date', 'reason', 'leave_type'}
