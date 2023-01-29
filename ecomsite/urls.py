"""ecomsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from shop import views
from rest_framework import routers
# from shop.views import ProductViewSet

# By including the router in the urlpatterns in the urls.py file, it can automatically create the appropriate URLs for the viewsets in the router, allowing us to easily access the viewsets through the URLs such as '/api/products/'

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)

urlpatterns = [
    #path to access admin to manage users and add products
    path('admin/', admin.site.urls),
    #backend simple display of products, simply styled
    path('', views.index, name='index'),
    #api path for customers
    path('api/customers/', views.customers, name='customers'),
    #ap path for products to add and returns json
    path('api/', include(router.urls)),
]
