# Generated by Django 3.2.25 on 2024-11-21 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='mobile_number',
            field=models.IntegerField(default=0.0),
            preserve_default=False,
        ),
    ]