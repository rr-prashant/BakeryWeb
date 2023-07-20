# Generated by Django 4.2.2 on 2023-07-11 18:00

import bakery_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bakery_app', '0004_alter_banner_banner_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='cakes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('cake_price', models.FloatField(max_length=100)),
                ('about_cake', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500)),
                ('cake_weight', models.CharField(max_length=100)),
                ('cake_toppings', models.CharField(max_length=100)),
                ('cake_extras', models.CharField(max_length=100)),
                ('accessory_image1', models.ImageField(upload_to='accessories_images/', validators=[bakery_app.models.validate_cake_image_dimensions])),
                ('accessory_image2', models.ImageField(upload_to='accessories_images/', validators=[bakery_app.models.validate_cake_image_dimensions])),
                ('accessory_image3', models.ImageField(upload_to='accessories_images/', validators=[bakery_app.models.validate_cake_image_dimensions])),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
            ],
        ),
    ]