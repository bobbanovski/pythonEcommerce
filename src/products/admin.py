from django.contrib import admin

# Register your models here.
from .models import Product

# Modify the Admin screen so that the below also shows up
class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug']
    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)