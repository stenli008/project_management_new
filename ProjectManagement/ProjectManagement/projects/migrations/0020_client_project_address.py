# Generated by Django 4.2.4 on 2023-08-18 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0019_task_progress'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=120)),
                ('last_name', models.CharField(max_length=120)),
                ('organisation', models.CharField(max_length=120)),
                ('phone_number', models.CharField(blank=True, max_length=120)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('address', models.CharField(max_length=120)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='address',
            field=models.CharField(default='default', max_length=120),
            preserve_default=False,
        ),
    ]
