from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404

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


#============ Detailed Views ========================
class ProductDetailView(DetailView):
    queryset = Product.objects.all() #retrieve from database
    template_name = "products/detail.html"
    #view context data - every clas based view has this method - gets the context
    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context

#Function based view
def product_detail_view(request, id=None, *args, **kwargs):
    # instance = Product.objects.get(pk=id)
    instance = get_object_or_404(Product, pk=id)
    context = {
        'object': instance
    }
    print(instance)
    return render(request, "products/detail.html", context)
