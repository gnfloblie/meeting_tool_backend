# Generated by Django 2.1.8 on 2019-05-28 15:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0004_auto_20190528_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 28, 15, 18, 9, 310876)),
        ),
    ]
