# Generated by Django 4.2.4 on 2023-08-18 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0020_client_project_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='projects.client'),
        ),
    ]
