# Generated by Django 5.1.3 on 2024-11-15 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_department_name_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='Document_endpath',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]