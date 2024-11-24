# Generated by Django 3.2.25 on 2024-11-21 05:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TravelPackage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('duration', models.IntegerField()),
                ('image', models.ImageField(upload_to='packages/')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('travel_date', models.DateField()),
                ('number_of_people', models.PositiveIntegerField()),
                ('customer_name', models.CharField(max_length=200)),
                ('customer_email', models.EmailField(max_length=254)),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel.travelpackage')),
            ],
        ),
    ]