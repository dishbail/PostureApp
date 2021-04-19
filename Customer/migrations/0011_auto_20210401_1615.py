# Generated by Django 2.2.5 on 2021-04-01 20:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0010_auto_20210401_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posturerecord',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 1, 20, 15, 11, 530657, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='sittingrecord',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 1, 20, 15, 11, 530657, tzinfo=utc), null=True),
        ),
    ]
