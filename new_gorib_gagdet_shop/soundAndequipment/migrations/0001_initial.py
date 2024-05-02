# Generated by Django 5.0.4 on 2024-04-30 03:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SoundCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='SoundDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='soundAndequipment/media/image')),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Description',
                'verbose_name_plural': 'Descriptions',
            },
        ),
        migrations.CreateModel(
            name='SoundWarranty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='soundSpecificaion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ChargingInterface', models.CharField(max_length=350)),
                ('Bluetooth', models.CharField(max_length=350)),
                ('StorageCapacity', models.CharField(max_length=350)),
                ('StorageType', models.CharField(max_length=350)),
                ('GraphicsModel', models.CharField(max_length=350)),
                ('Model', models.CharField(max_length=350)),
                ('Batterycapacity', models.CharField(max_length=350)),
                ('ANCStatus', models.CharField(max_length=350)),
                ('MicStatus', models.CharField(max_length=350)),
                ('DriverSize', models.CharField(blank=True, max_length=350, null=True)),
                ('SweatWaterResistance', models.CharField(blank=True, max_length=350, null=True)),
                ('WirelessCharging', models.CharField(max_length=350)),
                ('Playtime', models.CharField(max_length=350)),
                ('OtherFeaturesInfo', models.CharField(max_length=350)),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='soundAndequipment.soundcategory')),
            ],
        ),
        migrations.CreateModel(
            name='SoundAndequipmentProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('price', models.FloatField()),
                ('discount', models.FloatField()),
                ('status', models.CharField(blank=True, choices=[('In Stock ', 'In Stock'), ('Out of Stock', 'Out of Stock')], max_length=40, null=True)),
                ('image', models.ImageField(upload_to='soundAndequipment/media/image')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='soundAndequipment.soundcategory')),
                ('description', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='soundAndequipment.sounddescription')),
                ('specification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='soundAndequipment.soundspecificaion')),
                ('warranty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='soundAndequipment.soundwarranty')),
            ],
            options={
                'ordering': ['price'],
            },
        ),
    ]