# Generated by Django 4.2.4 on 2023-08-15 08:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('faqs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OtherApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_type', models.CharField(max_length=30)),
                ('request_description', models.TextField(max_length=300)),
                ('date', models.DateField(auto_now_add=True)),
                ('worker', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]