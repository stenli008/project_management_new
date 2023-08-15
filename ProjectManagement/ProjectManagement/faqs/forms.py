from django import forms

from ProjectManagement.faqs.models import LeaveApplication


class LeaveApplicationForm(forms.ModelForm):
    class Meta:
        model = LeaveApplication
        fields = {'reason', 'start_date', 'end_date', 'leave_type'}