# Generated by Django 4.0.3 on 2022-08-26 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_alter_recipe_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='step',
            name='food_items',
            field=models.ManyToManyField(blank=True, to='recipes.fooditem'),
        ),
    ]
