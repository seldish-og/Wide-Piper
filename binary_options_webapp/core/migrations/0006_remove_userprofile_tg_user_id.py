# Generated by Django 5.1.1 on 2024-09-07 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_userprofile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='tg_user_id',
        ),
    ]
