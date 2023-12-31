# Generated by Django 4.2.4 on 2023-08-16 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_alter_taskcategory_task_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskcategory',
            name='unit',
            field=models.CharField(choices=[('METERS', 'Meters'), ('NUMBER', 'Number')], default='default', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='taskcategory',
            name='task_category',
            field=models.CharField(max_length=30),
        ),
    ]
