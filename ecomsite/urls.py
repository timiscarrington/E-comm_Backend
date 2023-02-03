
from django.contrib import admin
from django.urls import path, include
from shop import views
from rest_framework import routers
from shop.views import MyTokenObtainPairView
from shop.views import CustomerModelBackend
from shop.views import login

# from shop.views import ProductViewSet

# By including the router in the urlpatterns in the urls.py file, it can automatically create the appropriate URLs for the viewsets in the router, allowing us to easily access the viewsets through the URLs such as '/api/products/'

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'carts', views.CartViewSet)


from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    #path to access admin to manage users and add products
    path('admin/', admin.site.urls),
    #backend simple display of products, simply styled
    path('', views.index, name='index'),
    #api path for customers
    path('api/customers/', views.customers, name='customers'),
    #api path for register a customer
    path('api/register/', views.register, name='register'),
    #api path for products to add and returns json
    path('api/', include(router.urls)),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('customer/login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/', login, name='login'),
    path('api/', include(router.urls)),
   
]
