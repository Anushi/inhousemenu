# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search_recipes', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Recipe',
            new_name='recipe_list',
        ),
    ]
