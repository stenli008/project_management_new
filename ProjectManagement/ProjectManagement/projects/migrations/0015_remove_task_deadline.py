# Generated by Django 4.2.4 on 2023-08-16 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0014_task_deadline'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='deadline',
        ),
    ]