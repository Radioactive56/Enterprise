# Generated by Django 5.1.3 on 2024-11-21 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_project_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
