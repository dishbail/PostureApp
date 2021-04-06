# Generated by Django 2.2.5 on 2021-03-10 15:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0008_auto_20210309_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posturerecord',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 10, 15, 4, 55, 700753, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='sittingrecord',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 10, 15, 4, 55, 700753, tzinfo=utc), null=True),
        ),
    ]