# Generated by Django 5.0 on 2023-12-28 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('empid', models.AutoField(primary_key=True, serialize=False)),
                ('empname', models.CharField(max_length=255)),
                ('device_working_condition', models.BooleanField(default=False)),
                ('device_name', models.CharField(blank=True, max_length=255, null=True)),
                ('os_version', models.CharField(blank=True, max_length=50, null=True)),
                ('location', models.CharField(choices=[('a', 'Location A'), ('b', 'Location B'), ('c', 'Location C'), ('d', 'Location D')], max_length=1)),
            ],
        ),
    ]