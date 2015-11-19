# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search_recipes', '0002_auto_20150921_1227'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecipeList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('recipe_name', models.TextField(null=True, blank=True)),
                ('source', models.CharField(max_length=50, null=True, blank=True)),
                ('url', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'recipe_list',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='recipe_list',
        ),
    ]
