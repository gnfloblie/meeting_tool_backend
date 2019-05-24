# Generated by Django 2.1.8 on 2019-05-24 19:32

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('participant', '0001_initial'),
        ('note', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notepad',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('project_name', models.CharField(default='', max_length=30)),
                ('title', models.CharField(default='', max_length=30)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2019, 5, 24, 19, 32, 8, 578835))),
                ('location', models.CharField(default='', max_length=30)),
                ('notes', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='note.Note')),
                ('participants', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='participant.Participant')),
            ],
        ),
    ]
