# Generated by Django 3.2.25 on 2024-11-21 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0002_booking_mobile_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travelpackage',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
