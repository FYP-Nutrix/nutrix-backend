# Generated by Django 3.2.13 on 2022-07-08 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_account_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='profile_pic',
            field=models.ImageField(blank=True, default='img/undraw_profile.svg', null=True, upload_to='img/profile'),
        ),
    ]
