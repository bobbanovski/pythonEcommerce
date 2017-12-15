from django.views.generic import ListView
from django.shortcuts import render

# Create your views here.
from .models import Product

#Class based view - List views
class ProductListView(ListView):
    queryset = Product.objects.all() #retrieve from database
    template_name = "products/list.html"
    #view context data - every clas based view has this method - gets the context
    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView, self).get_context_data(*args, **kwargs)
    #     print(context)
    #     return context

#Function based view
def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    print(queryset)
    return render(request, "products/list.html", context)
