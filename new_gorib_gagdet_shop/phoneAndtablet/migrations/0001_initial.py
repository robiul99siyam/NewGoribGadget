# Generated by Django 5.0.4 on 2024-04-29 15:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='PhoneColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='PhoneDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='phone_and_tablet/media/image')),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Description',
                'verbose_name_plural': 'Descriptions',
            },
        ),
        migrations.CreateModel(
            name='PhoneSpecification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=350)),
                ('network', models.CharField(max_length=350)),
                ('dimensions', models.CharField(max_length=350)),
                ('weight', models.CharField(max_length=350)),
                ('sim', models.CharField(max_length=350)),
                ('display_type', models.CharField(max_length=350)),
                ('display_size', models.CharField(max_length=350)),
                ('display_resolution', models.CharField(max_length=350)),
                ('os', models.CharField(max_length=350)),
                ('chipset', models.CharField(blank=True, max_length=350, null=True)),
                ('cpu', models.CharField(blank=True, max_length=350, null=True)),
                ('memory', models.CharField(max_length=350)),
                ('main_camera', models.CharField(max_length=350)),
                ('selfie_camera', models.CharField(max_length=350)),
                ('sound', models.CharField(max_length=350)),
                ('battery_info', models.CharField(max_length=350)),
                ('sensors', models.CharField(max_length=350)),
            ],
            options={
                'verbose_name': 'Specification',
                'verbose_name_plural': 'Specifications',
            },
        ),
        migrations.CreateModel(
            name='PhoneWarranty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('duration', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductStorage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='PhoneTabletProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('price', models.FloatField()),
                ('discount', models.FloatField()),
                ('status', models.CharField(choices=[('In Stock', 'In Stock'), ('Out Of Stock ', 'Out Of Stock ')], max_length=40)),
                ('sim', models.CharField(choices=[('Dual', 'Dual'), ('Single', 'Single')], max_length=40)),
                ('image', models.ImageField(upload_to='phoneAndtablet/media/image')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='phoneAndtablet.phonecategory')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='phoneAndtablet.phonecolor')),
                ('description', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='phoneAndtablet.phonedescription')),
                ('specification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='phoneAndtablet.phonespecification')),
                ('warranty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='phoneAndtablet.phonewarranty')),
            ],
            options={
                'ordering': ['price'],
            },
        ),
    ]
