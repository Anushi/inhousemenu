# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search_recipes', '0008_auto_20150922_1625'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='recipelist',
            table='recipe_list_images',
        ),
    ]
