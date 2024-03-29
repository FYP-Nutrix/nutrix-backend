# Generated by Django 3.2.13 on 2022-07-04 09:32

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('meal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nutrition',
            fields=[
                ('nutrition_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('meal_name', models.CharField(max_length=255)),
                ('carb', models.DecimalField(decimal_places=2, max_digits=7)),
                ('protein', models.DecimalField(decimal_places=2, max_digits=7)),
                ('fiber', models.DecimalField(decimal_places=2, max_digits=7)),
                ('fats', models.DecimalField(decimal_places=2, max_digits=7)),
                ('water', models.DecimalField(decimal_places=2, max_digits=7)),
                ('mineral', models.DecimalField(decimal_places=2, max_digits=7)),
                ('vitamin_a', models.DecimalField(decimal_places=2, max_digits=7)),
                ('vitamin_b', models.DecimalField(decimal_places=2, max_digits=7)),
                ('vitamin_c', models.DecimalField(decimal_places=2, max_digits=7)),
                ('vitamin_d', models.DecimalField(decimal_places=2, max_digits=7)),
                ('vitamin_e', models.DecimalField(decimal_places=2, max_digits=7)),
                ('vitamin_k', models.DecimalField(decimal_places=2, max_digits=7)),
                ('calorie_per_serving', models.IntegerField()),
                ('serving_size', models.DecimalField(decimal_places=2, max_digits=7)),
                ('serving_type', models.CharField(max_length=255)),
                ('serving_gram', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='NutritionLogging',
            fields=[
                ('nutrition_logging_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('meal_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meal.mealimage')),
                ('nutrition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nutrition.nutrition')),
            ],
        ),
    ]
