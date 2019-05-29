# Generated by Django 2.2.1 on 2019-05-29 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0004_auto_20190529_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='museum',
            name='DESCRIPTION',
            field=models.CharField(db_index=True, max_length=10000),
        ),
        migrations.AlterField(
            model_name='museum',
            name='PHOTOURL',
            field=models.CharField(db_index=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='museum',
            name='WEBURL',
            field=models.CharField(db_index=True, max_length=1000),
        ),
    ]
