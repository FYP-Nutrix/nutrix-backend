# Generated by Django 3.2.13 on 2022-07-08 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20220708_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='profile_pic',
            field=models.ImageField(blank=True, default='/img/undraw_profile.svg', null=True, upload_to='img/profile'),
        ),
    ]