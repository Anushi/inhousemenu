# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search_recipes', '0004_djangomigrations'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecipeIngredient',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('recipe_name', models.CharField(max_length=500, null=True, blank=True)),
                ('qty', models.CharField(max_length=50, null=True, blank=True)),
                ('amount', models.CharField(max_length=50, null=True, blank=True)),
                ('unit', models.CharField(max_length=50, null=True, blank=True)),
                ('ingredient', models.CharField(max_length=500, null=True, blank=True)),
                ('recipe_type', models.CharField(max_length=50, null=True, blank=True)),
                ('source', models.CharField(max_length=50, null=True, blank=True)),
            ],
            options={
                'db_table': 'recipe_ingredient',
                'managed': False,
            },
        ),
    ]
