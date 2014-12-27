# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='group',
            field=models.ForeignKey(related_name='member_set', to='groups.Group'),
            preserve_default=True,
        ),
    ]
