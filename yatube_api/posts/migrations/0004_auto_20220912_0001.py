# Generated by Django 2.2.16 on 2022-09-11 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20220911_2358'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follow',
            old_name='following',
            new_name='following_user',
        ),
    ]
