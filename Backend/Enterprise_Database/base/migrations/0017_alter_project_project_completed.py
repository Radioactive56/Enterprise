# Generated by Django 5.1.4 on 2025-01-15 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_alter_task_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_completed',
            field=models.CharField(choices=[('Completed', 'Completed'), ('Not Completed', 'Not Completed')], default='Not Completed', max_length=128),
        ),
    ]
