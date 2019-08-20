# Generated by Django 2.1.5 on 2019-08-20 13:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=100)),
                ('opening_time', models.DateTimeField(default=datetime.datetime.now)),
                ('closing_time', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
