from django.shortcuts import render
from .models import Customer
from django.http import JsonResponse
from shop.serializers import CustomerSerializer
from rest_framework import viewsets, generics
from .models import Products
from .serializers import ProductSerializer
from django.core.paginator import Paginator
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


def index(request):
    product_objects = Products.objects.all()
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        product_objects = product_objects.filter(title__icontains=item_name)

    paginator = Paginator(product_objects, 4)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)

    return render(request, 'shop/index.html', {'product_objects':product_objects})
   


def customers(request):
    data = Customer.objects.all()
    serializer = CustomerSerializer(data, many=True)
    return JsonResponse({'customers': serializer.data})


@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    

    def get_permissions(self):
        return super(ProductViewSet, self).get_permissions()
