from django.db import models

# Create your models here.
# Connect Django to database
# Save changes with python manage.py makemigrations
# python manage.py migrate
class Product(models.Model):
    title       = models.CharField(max_length=120) #Charfields always have size limits
    description = models.TextField()
    price       = models.DecimalField(decimal_places=2, max_digits=20, default=39.99)

