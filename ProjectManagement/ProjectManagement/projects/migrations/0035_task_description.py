# Generated by Django 4.2.4 on 2023-08-21 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0034_taskcategory_action_taskcategory_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True, max_length=300),
        ),
    ]
