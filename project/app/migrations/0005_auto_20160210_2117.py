# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20160209_2015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='buycharac',
        ),
        migrations.AddField(
            model_name='item',
            name='amor',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='amortization'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='item',
            name='gib',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='gibkost'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='item',
            name='komp',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='kompaktnost'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='item',
            name='speed',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='speed'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='item',
            name='upr',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='upravlyaemost'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='item',
            name='ust',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='ustoychivost'),
            preserve_default=True,
        ),
    ]
