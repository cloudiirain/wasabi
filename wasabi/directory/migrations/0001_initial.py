# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('order', models.IntegerField()),
                ('body', models.TextField()),
                ('owner', models.ForeignKey(related_name='chapters', default=None, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['series', 'order'],
            },
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=100)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.AddField(
            model_name='chapter',
            name='series',
            field=models.ForeignKey(related_name='chapters', to='directory.Series'),
        ),
        migrations.AlterUniqueTogether(
            name='chapter',
            unique_together=set([('series', 'title')]),
        ),
    ]
