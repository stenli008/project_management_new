# Generated by Django 4.2.4 on 2023-08-15 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_leaveapplication_leave_type_leaveapplication_status'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LeaveApplication',
        ),
    ]
