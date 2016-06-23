# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160518_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='like_count',
            field=models.IntegerField(default=0),
        ),
    ]
