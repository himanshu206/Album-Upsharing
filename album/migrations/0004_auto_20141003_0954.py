# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0003_auto_20141003_0947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albumphotos',
            name='photo',
            field=models.ImageField(upload_to='../static/user_images/'),
        ),
    ]
