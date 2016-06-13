# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20160202_2026'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='buycharac',
            field=models.TextField(default='hello', verbose_name='Buylongboard characteristics'),
            preserve_default=False,
        ),
    ]
