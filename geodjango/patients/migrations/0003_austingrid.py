# Generated by Django 3.0 on 2019-12-13 03:20

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0002_auto_20191208_2242'),
    ]

    operations = [
        migrations.CreateModel(
            name='AustinGrid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField(default=0)),
                ('mpoly', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
    ]
