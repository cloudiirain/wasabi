# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('order', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='page',
            name='series',
            field=models.ForeignKey(to='directory.Series'),
        ),
        migrations.AlterUniqueTogether(
            name='page',
            unique_together=set([('series', 'title')]),
        ),
    ]
