# Generated by Django 3.2.13 on 2022-08-01 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meal', '0007_alter_mealimage_meal_logging'),
    ]

    operations = [
        migrations.AddField(
            model_name='mealimage',
            name='meal_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
