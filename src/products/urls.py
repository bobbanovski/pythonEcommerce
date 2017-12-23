#relative urls
from django.conf.urls import url

from products.views import (
    ProductListView, 
    # product_list_view, 
    ProductDetailView, 
    ProductDetailSlugView,
    # product_detail_view, 
    # ProductFeaturedListView, 
    # ProductFeaturedDetailView
)

urlpatterns = [
    # url(r'^featured/$', ProductFeaturedListView.as_view()), #.as_view needed to prevent error: __init__() takes 1 positional argument but 2
    # url(r'^featured/(?P<id>\d+)/$', ProductFeaturedDetailView.as_view()),
    url(r'^$', ProductListView.as_view()),
    # url(r'products-fbv/$', product_list_view),
    # url(r'product/(?P<id>\d+)/$', ProductDetailView.as_view()), #id is kwarg
    url(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view()), 
    # url(r'product-fbv/(?P<id>\d+)/$', product_detail_view),
]

    
