from django.shortcuts import render
from .models import Customer
from django.http import JsonResponse
from shop.serializers import CustomerSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, AllowAny
from .models import Products
from .serializers import ProductSerializer
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    product_objects = Products.objects.all()
# performing a search for item name, and then letting it be lenient by filtering and seeing if the search contains a similar name
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        product_objects = product_objects.filter(title__icontains=item_name)

         # pagination to display the products
    paginator = Paginator(product_objects, 4)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)

    return render(request, 'shop/index.html', {'product_objects':product_objects})
   


def customers(request):
    data = Customer.objects.all()
    serializer = CustomerSerializer(data, many=True)
    return JsonResponse({'customers': serializer.data})

# a class called ProductViewSet which inherits from viewsets.ModelViewSet.This class defines the queryset and serializer_class attributes. The queryset attribute is set to Products.objects.all() which will retrieve all the products from the Products model. The serializer_class attribute is set to ProductSerializer.

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser | AllowAny]
    #function that checks if its admin user, if not products can only be read, not updated, created, nor destroyed
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAdminUser]
        return super(ProductViewSet, self).get_permissions()
