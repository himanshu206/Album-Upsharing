# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0002_auto_20141003_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albumphotos',
            name='photo',
            field=models.ImageField(upload_to='user_images/'),
        ),
    ]
