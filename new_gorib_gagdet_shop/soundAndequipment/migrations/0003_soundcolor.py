# Generated by Django 5.0.4 on 2024-04-30 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soundAndequipment', '0002_soundplug_soundtype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Soundcolor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250)),
            ],
        ),
    ]