# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search_recipes', '0007_auto_20150922_1621'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='recipecontent2',
            table='recipe_content_2',
        ),
    ]
