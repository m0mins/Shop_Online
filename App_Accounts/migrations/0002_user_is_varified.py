# Generated by Django 4.2.5 on 2023-12-18 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_varified',
            field=models.BooleanField(default=False),
        ),
    ]
