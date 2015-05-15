# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='fullname',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='notes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='points',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='username',
            field=models.IntegerField(default=0),
        ),
    ]
