# Generated by Django 2.1.5 on 2019-01-29 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Occurrence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('plan', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('traffic_ticket', models.TextField()),
                ('drivers_licence', models.TextField()),
                ('dut_copy', models.TextField()),
                ('value', models.FloatField()),
            ],
        ),
    ]
