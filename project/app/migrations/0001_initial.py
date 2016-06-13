# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=40, verbose_name='name')),
                ('price', models.PositiveIntegerField(blank=True, null=True)),
                ('picture', models.ImageField(blank=True, upload_to='to/', verbose_name='picture')),
                ('site', models.URLField(blank=True)),
                ('charac', models.TextField(verbose_name='characteristics')),
            ],
            options={
                'verbose_name_plural': 'Items',
                'verbose_name': 'Item',
            },
            bases=(models.Model,),
        ),
    ]
