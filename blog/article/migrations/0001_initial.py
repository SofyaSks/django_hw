# Generated by Django 5.2.1 on 2025-05-20 10:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('text', models.CharField(max_length=100000)),
                ('dt', models.DateTimeField(blank=True, default=datetime.datetime(2025, 5, 20, 13, 4, 50, 164409))),
            ],
        ),
    ]
