# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='trips',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('trip_id', models.CharField(max_length=255)),
                ('trip_data', models.TextField()),
            ],
        ),
    ]
