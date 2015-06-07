# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('symbol', models.CharField(unique=True, max_length=10)),
                ('name', models.CharField(max_length=24)),
                ('last_sale', models.FloatField()),
                ('market_cap', models.CharField(max_length=12)),
                ('ipo_year', models.CharField(max_length=4)),
                ('sector', models.CharField(max_length=22)),
                ('industry', models.CharField(max_length=64)),
                ('summary_quote', models.URLField()),
            ],
        ),
    ]
