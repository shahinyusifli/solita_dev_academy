# Generated by Django 4.0 on 2022-01-02 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Farms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=150)),
                ('date_time', models.DateTimeField()),
                ('sensor_type', models.CharField(max_length=50)),
                ('values', models.IntegerField()),
            ],
        ),
    ]
