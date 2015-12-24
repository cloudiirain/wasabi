# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('directory', '0002_page_owner'),
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
                ('series', models.ForeignKey(related_name='chapters', to='directory.Series')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='page',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='page',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='page',
            name='series',
        ),
        migrations.DeleteModel(
            name='Page',
        ),
        migrations.AlterUniqueTogether(
            name='chapter',
            unique_together=set([('series', 'title')]),
        ),
    ]
