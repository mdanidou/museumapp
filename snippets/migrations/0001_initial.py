# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CATEGORY',
            fields=[
                ('CATEGORYNAME', models.CharField(db_index=True, max_length=200)),
                ('CATEGORYID', models.IntegerField(serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='PRICE',
            fields=[
                ('PRICENAME', models.CharField(db_index=True, max_length=200)),
                ('PRICEID', models.IntegerField(serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('NAME', models.CharField(db_index=True, max_length=200)),
                ('DESCRIPTION', models.TextField(blank=True)),
                ('COUNTRY', models.CharField(db_index=True, max_length=200)),
                ('STATE', models.CharField(db_index=True, max_length=200)),
                ('CITY', models.CharField(db_index=True, max_length=200)),
                ('ADDRESS', models.CharField(db_index=True, max_length=200)),
                ('TK', models.DateTimeField(auto_now_add=True)),
                ('PHONE', models.IntegerField(blank=True)),
                ('WEBURL', models.URLField(max_length=250)),
                ('PHOTOURL', models.URLField(max_length=250)),
                ('MAP', models.CharField(db_index=True, max_length=200)),
                ('CATEGORYID', models.ForeignKey(on_delete=models.deletion.CASCADE, related_name='CATEGORY', to='snippets.CATEGORY')),
                ('PRICEID', models.ForeignKey(on_delete=models.deletion.CASCADE, related_name='PRICE', to='snippets.PRICE')),
            ],
            options={
                'ordering': ('NAME', 'TK'),
            },
        ),
    ]
