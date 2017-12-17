from django.http import Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Product

class ProductFeaturedListView(ListView):
    template_name = "products/list.html"
    def get_queryset(self, *args, **kwargs):
        request = self.request
        print(Product.objects.featured())
        return Product.objects.featured()

class ProductFeaturedDetailView(DetailView):
    queryset = Product.objects.featured()
    template_name = "products/featured-detail.html"

    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     return Product.objects.featured()

    #Below is needed to call with object pk
    def get_object(self, *args, **kwargs):
        request = self.request
        id = self.kwargs.get('id')
        instance = Product.objects.get_by_id(id)
        print(instance)
        return instance

#Class based view - List views
class ProductListView(ListView):
    # queryset = Product.objects.all() #retrieve from database
    template_name = "products/list.html"
    #view context data - every clas based view has this method - gets the context
    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView, self).get_context_data(*args, **kwargs)
    #     print(context)
    #     return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()

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
    # queryset = Product.objects.all() #retrieve from database
    template_name = "products/detail.html"
    #view context data - every clas based view has this method - gets the context
    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        id = self.kwargs.get('id')
        instance = Product.objects.get_by_id(id)
        print(instance)
        if instance is None:
            raise Http404("Product not found")
        # return instance
        context = {
        'object': instance
        }
        return instance

#Function based view
def product_detail_view(request, id=None, *args, **kwargs):
    # instance = Product.objects.get(pk=id)
    # instance = get_object_or_404(Product, pk=id)
    #above or below are equivalent
    # try:
    #     instance = Product.objects.get(id=id)
    # except Product.DoesNotExist:
    #     print('no product found')
    #     raise Http404("Product not found")
    # except:
    #     print('wat')

    instance = Product.objects.get_by_id(id)
    print(instance)
    if instance is None:
        raise Http404("Product not found")
# objects is a model manager
# filter is model manager method
    # qs = Product.objects.filter(id=id) 
    # if qs.exists() and qs.count() == 1:
    #     instance = qs.first()
    # else:
    #     raise Http404("Product not found")

    context = {
        'object': instance
    }
    # print(instance)
    return render(request, "products/detail.html", context)
