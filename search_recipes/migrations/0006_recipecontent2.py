# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search_recipes', '0005_recipeingredient'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecipeContent2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('recipe_id', models.IntegerField()),
                ('recipe_name', models.TextField()),
                ('content', models.TextField()),
                ('recipe_type', models.CharField(max_length=50)),
                ('taste', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'recipe_content_2',
                'managed': False,
            },
        ),
    ]
