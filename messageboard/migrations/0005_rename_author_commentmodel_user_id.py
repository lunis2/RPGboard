# Generated by Django 4.1.7 on 2023-03-22 02:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messageboard', '0004_commentmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commentmodel',
            old_name='author',
            new_name='user_id',
        ),
    ]
