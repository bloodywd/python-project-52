# Generated by Django 5.1.1 on 2024-09-28 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_rename_task_perfomer_task_executor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='label',
            new_name='labels',
        ),
    ]
