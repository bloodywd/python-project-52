# Generated by Django 5.1.1 on 2024-09-28 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_task_label_alter_task_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='task_perfomer',
            new_name='executor',
        ),
    ]