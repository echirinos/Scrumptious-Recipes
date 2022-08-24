from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=125, null=True)
    author = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    image = models.URLField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name + " by " + self.author


class Measure(models.Model):
    name = models.CharField(max_length=30, unique=True)
    abbreviation = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name + " cups equals " + self.abbreviation + " teaspoons"


class FoodItem(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    amount = models.FloatField(float)
    recipe = models.ForeignKey(
        "Recipe", related_name="ingredients", on_delete=models.CASCADE
    )
    measure = models.ForeignKey("Measure", on_delete=models.PROTECT)
    food = models.ForeignKey("FoodItem", on_delete=models.PROTECT)

    def __str__(self):
        return (
            self.amount
            + " "
            + self.recipe
            + +" "
            + self.measure
            + " "
            + self.food
        )


class Step(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        related_name="steps",
        on_delete=models.CASCADE,
    )
    order = models.PositiveIntegerField()
    directions = models.CharField(max_length=300)


def __str__(self):
    return " " + self.recipe + " " + self.order + " " + self.directions


# update models
# 1. update the model or create the model
# class Recipe(models.Model):
#    pass

# 2. Make migrations, which makes initial fuile
# python manage.py makemigrations

# 3. python manage.py migrate: It takes python code
# that was generated and will make a table
