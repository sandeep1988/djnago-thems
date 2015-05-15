# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20150507_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='username',
            field=models.CharField(max_length=200),
        ),
    ]
