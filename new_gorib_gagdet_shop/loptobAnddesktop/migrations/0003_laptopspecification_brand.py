# Generated by Django 5.0.4 on 2024-04-30 03:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loptobAnddesktop', '0002_alter_laptobanddesktopproduct_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='laptopspecification',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='loptobAnddesktop.laptopcategory'),
        ),
    ]