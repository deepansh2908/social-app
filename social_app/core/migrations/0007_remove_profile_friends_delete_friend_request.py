# Generated by Django 5.0.1 on 2024-01-03 05:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_profile_friends_alter_profile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='friends',
        ),
        migrations.DeleteModel(
            name='Friend_request',
        ),
    ]
