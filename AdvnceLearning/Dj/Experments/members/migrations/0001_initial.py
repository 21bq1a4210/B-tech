# Generated by Django 5.0 on 2023-12-12 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('char_field', models.CharField(blank=True, max_length=255, null=True)),
                ('int_field', models.IntegerField(blank=True, null=True)),
                ('float_field', models.FloatField(blank=True, null=True)),
                ('decimal_field', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('date_field', models.DateField(blank=True, null=True)),
                ('time_field', models.TimeField(blank=True, null=True)),
                ('datetime_field', models.DateTimeField(blank=True, null=True)),
                ('boolean_field', models.BooleanField(default=True)),
                ('email_field', models.EmailField(blank=True, max_length=255, null=True)),
                ('url_field', models.URLField(blank=True, max_length=255, null=True)),
                ('image_field', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('file_field', models.FileField(blank=True, null=True, upload_to='files/')),
                ('text_field', models.TextField(blank=True, null=True)),
                ('slug_field', models.SlugField(blank=True, max_length=255, null=True)),
                ('binary_field', models.BinaryField(blank=True, null=True)),
                ('uuid_field', models.UUIDField(blank=True, null=True)),
            ],
        ),
    ]
