# Generated by Django 5.0.4 on 2024-04-30 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('powerAndaccessories', '0004_remove_powerwarranty_duration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='powertabletproduct',
            name='Warranty',
        ),
        migrations.DeleteModel(
            name='PowerWarranty',
        ),
    ]