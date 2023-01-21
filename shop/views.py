from django.shortcuts import render
from .models import Customer
from django.http import JsonResponse
from shop.serializers import CustomerSerializer
from rest_framework import viewsets
from .models import Products
from .serializers import ProductSerializer

# Create your views here.

def index(request):
    product_objects = Products.objects.all()
# performing a search for item name, and then letting it be lenient by filtering and seeing if the search contains a similar name
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        product_objects = product_objects.filter(title__icontains=item_name)
    return render(request, 'shop/index.html', {'product_objects':product_objects})

def customers(request):
    data = Customer.objects.all()
    serializer = CustomerSerializer(data, many=True)
    return JsonResponse({'customers': serializer.data})

# a class called ProductViewSet which inherits from viewsets.ModelViewSet.This class defines the queryset and serializer_class attributes. The queryset attribute is set to Products.objects.all() which will retrieve all the products from the Products model. The serializer_class attribute is set to ProductSerializer.

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
 