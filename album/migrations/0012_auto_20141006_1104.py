# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0011_auto_20141006_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albumphotos',
            name='photo',
            field=models.ImageField(upload_to='user_images/'),
        ),
    ]
