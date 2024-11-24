# travel_package/models.py
from django.db import models

class TravelPackage(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.IntegerField()  # Duration in days
    image = models.ImageField()
    
    def __str__(self):
        return self.name

class Booking(models.Model):
    package = models.ForeignKey(TravelPackage, on_delete=models.CASCADE)
    travel_date = models.DateField()
    number_of_people = models.PositiveIntegerField()
    customer_name = models.CharField(max_length=200)
    customer_email = models.EmailField()
    mobile_number = models.IntegerField()
    
    def __str__(self):
        return f"Booking for {self.customer_name} on {self.travel_date}"
    
"""
class PackageImage(models.Model):
    package = models.ForeignKey(TravelPackage, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='package_images/')
    
    def __str__(self):
        return f"Image for {self.package.name}"""
