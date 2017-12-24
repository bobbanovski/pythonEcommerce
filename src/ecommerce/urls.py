"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url,include
from django.contrib import admin
from .views import (home_page, about_page, contact_page, login_page, register_page)

from carts.views import cart_home

from products.views import (
    ProductListView, 
    product_list_view, 
    ProductDetailView, 
    ProductDetailSlugView, 
    product_detail_view, 
    ProductFeaturedListView, 
    ProductFeaturedDetailView)

# Forgetting the ^ for the regex here will have serious consequences
urlpatterns = [
    url(r'^$', home_page, name='home'),
    url(r'^about/$', about_page, name='about'),
    url(r'^contact/$', contact_page, name='contact'),
    url(r'^login/$', login_page, name='login'),
    url(r'^register/$', register_page, name='register'),
    url(r'^featured/$', ProductFeaturedListView.as_view()), #.as_view needed to prevent error: __init__() takes 1 positional argument but 2
    url(r'^featured/(?P<id>\d+)/$', ProductFeaturedDetailView.as_view()),
    url(r'^products/', include("products.urls", namespace='products')),
    url(r'^products/$', ProductListView.as_view()),
    url(r'^products-fbv/$', product_list_view),
    # url(r'^product/(?P<id>\d+)/$', ProductDetailView.as_view()), #id is kwarg
    url(r'^products/(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view()),    
    url(r'^product-fbv/(?P<id>\d+)/$', product_detail_view),
    url(r'^cart/$', cart_home, name='cart'),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG: #This is set up in settings.py
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
