# Generated by Django 3.2.13 on 2022-07-08 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='id',
            new_name='user_id',
        ),
    ]