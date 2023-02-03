from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from rest_framework import viewsets, generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import Customer, Products, Cart
from .serializers import CustomerSerializer, ProductSerializer, CartSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        customer = authenticate(email=email, password=password)

        if customer is None or not customer.is_active:
            raise serializers.ValidationError('Unable to log in with provided credentials.')

        return {
            'token': customer.token,
            'user_id': customer.pk,
            'email': customer.email,
        }

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


def index(request):
    product_objects = Products.objects.all()
    item_name = request.GET.get('item_name')
    if item_name:
        product_objects = product_objects.filter(title__icontains=item_name)

    paginator = Paginator(product_objects, 4)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)

    return render(request, 'shop/index.html', {'product_objects': product_objects})


@api_view(['GET'])
def customers(request):
    data = Customer.objects.all()
    serializer = CustomerSerializer(data, many=True)
    return Response({'customers': serializer.data})

@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        return super().get_permissions()


class CustomerModelBackend(APIView):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = Customer.objects.get(email=email)
            if user.check_password(password):
                return user
        except Customer.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Customer.objects.get(pk=user_id)
        except Customer.DoesNotExist:
            return None

@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        email = request.data.get('email')
        password = request.data.get('password')
        user = CustomerModelBackend().authenticate(request, email=email, password=password)
        if user:
            serializer = CustomerSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = []

    def get_permissions(self):
        return []

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def carts(request):
    if request.method == 'GET':
        data = Cart.objects.all()
        serializer = CartSerializer(data, many=True)
        return Response({'carts': serializer.data})

    if request.method == 'POST':
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        data = Cart.objects.get(id=request.data['id'])
        serializer = CartSerializer(instance=data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        data = Cart.objects.get(id=request.data['id'])
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
