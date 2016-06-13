# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_item_buycharac'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='buycharac',
            field=models.TextField(blank=True, null=True, verbose_name='Buylongboard characteristics'),
        ),
        migrations.AlterField(
            model_name='item',
            name='charac',
            field=models.TextField(blank=True, null=True, verbose_name='characteristics'),
        ),
    ]
