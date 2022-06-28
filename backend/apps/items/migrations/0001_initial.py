# Generated by Django 4.0.2 on 2022-06-15 03:12

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], db_index=True, default='inactive', max_length=15, verbose_name='status')),
                ('name', models.CharField(db_index=True, default='anonymous', max_length=20, verbose_name='Name')),
                ('price', models.DecimalField(decimal_places=2, max_digits=14, verbose_name='price')),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
            ],
            options={
                'db_table': 'item',
            },
        ),
    ]
