# Generated by Django 4.2.4 on 2023-08-21 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0032_alter_task_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]