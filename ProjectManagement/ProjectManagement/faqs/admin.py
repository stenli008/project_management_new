from django.contrib import admin

from ProjectManagement.faqs.models import LeaveApplication, OtherApplication

admin.site.register(LeaveApplication)
admin.site.register(OtherApplication)
