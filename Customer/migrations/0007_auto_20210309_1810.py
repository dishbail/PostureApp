# Generated by Django 3.0.7 on 2021-03-09 23:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0006_auto_20210307_1811'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='email',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='last_name',
        ),
        migrations.AlterField(
            model_name='customer',
            name='facebook',
            field=models.URLField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='github',
            field=models.URLField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='instagram',
            field=models.URLField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='twitter',
            field=models.URLField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='website',
            field=models.URLField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='posturerecord',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 9, 23, 10, 2, 970238, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='sittingrecord',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 9, 23, 10, 2, 970238, tzinfo=utc), null=True),
        ),
    ]
