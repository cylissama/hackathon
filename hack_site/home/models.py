from django.db import models

class Complaint(models.Model):
    # Auto-increment ID field is added automatically by Django as the primary key
    filer_name = models.CharField(max_length=100, verbose_name="Filer Name")
    email_address = models.EmailField(verbose_name="Email Address")
    phone_number = models.CharField(max_length=20, verbose_name="Phone Number")
    reason_for_complaint = models.TextField(verbose_name="Reason for Complaint")

    def __str__(self):
        return f"Complaint by {self.filer_name}"
    
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Vendor(models.Model):
    name = models.CharField(max_length=255)
    categories = models.ManyToManyField(Category)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class PointOfInterest(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name
    
class Pass(models.Model):
    name = models.CharField(max_length=100)
    county = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.county})"
    
class Route(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=7, help_text="Hex color code for the route")
    points = models.ManyToManyField(PointOfInterest, related_name='routes')

    def __str__(self):
        return self.name

