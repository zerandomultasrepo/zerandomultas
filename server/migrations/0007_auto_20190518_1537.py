# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-05-18 15:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0006_auto_20190518_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='occurrence',
            name='drivers_licence',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='occurrence',
            name='dut_copy',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='occurrence',
            name='traffic_ticket',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
