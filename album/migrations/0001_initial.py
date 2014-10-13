# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AlbumInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('albumName', models.CharField(max_length=256)),
                ('date', models.DateField()),
                ('count', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AlbumPhotos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('photo', models.ImageField(upload_to='user_images/')),
                ('albumPhoto', models.ForeignKey(to='album.AlbumInfo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='saveRegister',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('f_name', models.CharField(max_length=256)),
                ('l_name', models.CharField(max_length=256)),
                ('email', models.CharField(max_length=256)),
                ('password', models.CharField(max_length=256)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='albuminfo',
            name='user',
            field=models.ForeignKey(to='album.saveRegister'),
            preserve_default=True,
        ),
    ]
