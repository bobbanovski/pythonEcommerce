from django.db import models
import os
import random

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    print(instance)
    print(filename)
    new_filename = random.randint(1,98746734)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "products/{new_filename}/{final_filename}".format(
        new_filename=new_filename, 
        final_filename=final_filename)

class ProductManager(models.Manager):
    def featured(self):
        qs = self.get_queryset().filter(featured=True)
        print(qs)
        return qs

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first() #Individual object
        return None

# Create your models here.
# Connect Django to database
# Save changes with python manage.py makemigrations
# python manage.py migrate
class Product(models.Model):
    title       = models.CharField(max_length=120) #Charfields always have size limits
    description = models.TextField()
    price       = models.DecimalField(decimal_places=2, max_digits=20, default=39.99)
    image       = models.ImageField(upload_to=upload_image_path, null=True, blank=True) #blank - not needed in django
    featured    = models.BooleanField(default=False)

    #Link above product manager to this model
    objects = ProductManager()

    #Needed to return title in admin
    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title