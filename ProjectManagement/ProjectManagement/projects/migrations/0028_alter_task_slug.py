# Generated by Django 4.2.4 on 2023-08-18 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0027_task_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
