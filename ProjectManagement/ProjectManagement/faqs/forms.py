from django import forms

from ProjectManagement.faqs.models import LeaveApplication, OtherApplication


class LeaveApplicationForm(forms.ModelForm):
    class Meta:
        model = LeaveApplication
        fields = {'reason', 'start_date', 'end_date', 'leave_type'}


class OtherApplicationForm(forms.ModelForm):
    class Meta:
        model = OtherApplication
        fields = {'request_type', 'request_description'}
