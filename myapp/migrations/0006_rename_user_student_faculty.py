# Generated by Django 4.2.5 on 2023-12-06 06:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_delete_user_student_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='user',
            new_name='faculty',
        ),
    ]