# Generated by Django 4.2.4 on 2023-08-16 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_taskcategory_unit_alter_taskcategory_task_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskcategory',
            name='unit',
            field=models.CharField(choices=[('METERS', 'Meters'), ('Quantity', 'Quantity')], max_length=100),
        ),
    ]
