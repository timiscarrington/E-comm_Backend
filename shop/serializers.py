from rest_framework import serializers
from shop.models import Customer
from shop.models import Products

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


# This class defines the fields attribute which specifies the fields of the Products model that should be included in the serialized representation.
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('id', 'title', 'price', 'category', 'description', 'image', 'image2', 'qty')

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Customer.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
