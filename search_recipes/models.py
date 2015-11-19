# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class RecipeIngredient(models.Model):
    id = models.IntegerField(primary_key=True)
    recipe_name = models.CharField(max_length=500, blank=True, null=True)
    qty = models.CharField(max_length=50, blank=True, null=True)
    amount = models.CharField(max_length=50, blank=True, null=True)
    unit = models.CharField(max_length=50, blank=True, null=True)
    ingredient = models.CharField(max_length=500, blank=True, null=True)
    recipe_type = models.CharField(max_length=50, blank=True, null=True)
    source = models.CharField(max_length=50, blank=True, null=True)
    taste = models.CharField(max_length=50)
    category = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'recipe_ingredient_2'


class RecipeList(models.Model):
    recipe_name = models.TextField(blank=True, null=True)
    source = models.CharField(max_length=50, blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    recipe_type = models.CharField(max_length=50, blank=True, null=True)
    taste = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    rank = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'recipe_list_images_tags'

class RecipeContent2(models.Model):
    recipe_id = models.IntegerField()
    recipe_name = models.TextField()
    content = models.TextField()
    recipe_type = models.CharField(max_length=50)
    taste = models.CharField(max_length=50)
    category = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'recipe_content_3'

class IngredientList(models.Model):
    id = models.IntegerField(primary_key=True)
    ingredient_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ingredients_recipekey_site'
