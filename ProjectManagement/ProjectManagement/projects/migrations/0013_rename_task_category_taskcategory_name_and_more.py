# Generated by Django 4.2.4 on 2023-08-16 18:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_task_task_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='taskcategory',
            old_name='task_category',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='task',
            name='task_name',
        ),
        migrations.AddField(
            model_name='task',
            name='requirement',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='taskcategory',
            name='unit',
            field=models.CharField(choices=[('METERS', 'Meters'), ('NUMBER', 'Number')], max_length=100),
        ),
    ]
