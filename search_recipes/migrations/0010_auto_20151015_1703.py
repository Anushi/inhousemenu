# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search_recipes', '0009_auto_20151015_1654'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='recipecontent2',
            table='recipe_content_3',
        ),
        migrations.AlterModelTable(
            name='recipeingredient',
            table='recipe_ingredient_2',
        ),
    ]
