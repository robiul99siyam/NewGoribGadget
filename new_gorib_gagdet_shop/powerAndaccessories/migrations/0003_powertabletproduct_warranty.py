# Generated by Django 5.0.4 on 2024-04-30 11:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('powerAndaccessories', '0002_remove_powertabletproduct_warranty'),
    ]

    operations = [
        migrations.AddField(
            model_name='powertabletproduct',
            name='Warranty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='powerAndaccessories.powerwarranty'),
        ),
    ]
