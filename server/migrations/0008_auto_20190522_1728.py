# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-05-22 17:28
from __future__ import unicode_literals

from django.db import migrations, models
import server.models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0007_auto_20190518_1537'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('comment', models.TextField()),
                ('accepted', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='occurrence',
            name='drivers_licence',
            field=models.ImageField(blank=True, null=True, upload_to=server.models.Occurrence.get_upload_path),
        ),
        migrations.AlterField(
            model_name='occurrence',
            name='dut_copy',
            field=models.ImageField(blank=True, null=True, upload_to=server.models.Occurrence.get_upload_path),
        ),
        migrations.AlterField(
            model_name='occurrence',
            name='traffic_ticket',
            field=models.ImageField(blank=True, null=True, upload_to=server.models.Occurrence.get_upload_path),
        ),
    ]
