# Generated by Django 4.0.3 on 2022-08-25 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_alter_recipe_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.TextField(),
        ),
    ]
