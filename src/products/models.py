from django.db import models
import os
import random
#Call a signal before an object is generated so that it can be incorporated
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .utils import unique_slug_generator
from django.urls import reverse

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

class ProductQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def featured(self):
        return self.filter(featured=True, active=True)

class ProductManager(models.Manager):
    #These are overrides for existing db commands
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()

    def featured(self):
        qs = self.get_queryset().filter(featured=True)
        print(qs)
        return qs

    # def features(self):
    #     return self.get_queryset().featured()
    #     # print(qs)
    #     # return qs

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
    slug        = models.SlugField(default='abc', unique=True)
    description = models.TextField()
    price       = models.DecimalField(decimal_places=2, max_digits=20, default=39.99)
    image       = models.ImageField(upload_to=upload_image_path, null=True, blank=True) #blank - not needed in django
    featured    = models.BooleanField(default=False)
    active      = models.BooleanField(default=True)

    #Link above product manager to this model
    objects = ProductManager()

    def get_absolute_url(self):
        # return "/products/{slug}".format(slug=self.slug)
        #more robust
        return reverse("products:detail", kwargs={"slug": self.slug})

    #Needed to return title in admin
    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title
    
    # def pre_save(sender, instance, **kwargs):
    #Create the signal action

def product_pre_save_receiver(sender, instance, *args, **kwargs):
    print(instance)
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
    # # Link the signal to the Product model
pre_save.connect(product_pre_save_receiver, sender=Product)

class NewProduct(models.Model):
    title       = models.CharField(max_length=120) #Charfields always have size limits
    description = models.TextField()
    price       = models.DecimalField(decimal_places=2, max_digits=20, default=39.99)
    image       = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    featured    = models.BooleanField(default=False)
    active      = models.BooleanField(default=True)
