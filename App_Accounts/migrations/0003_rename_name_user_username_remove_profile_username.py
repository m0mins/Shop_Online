# Generated by Django 4.2.5 on 2023-12-19 05:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_Accounts', '0002_user_is_varified'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='username',
        ),
    ]