# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search_recipes', '0011_auto_20151019_0959'),
    ]

    operations = [
        migrations.CreateModel(
            name='IngredientList',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('ingredient_name', models.CharField(max_length=100, null=True, blank=True)),
            ],
            options={
                'db_table': 'ingredients_recipekey_site',
                'managed': False,
            },
        ),
    ]
