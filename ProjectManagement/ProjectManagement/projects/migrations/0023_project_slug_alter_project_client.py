# Generated by Django 4.2.4 on 2023-08-18 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0022_alter_client_address_alter_client_organisation'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='slug',
            field=models.SlugField(default='default'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='projects.client'),
        ),
    ]