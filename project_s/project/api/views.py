from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import (
    User, FarmerProfile, CustomerProfile, Product, Order, OrderItem, Payment,
    CertificationRequest, Review, FAQ, ContactForm, Blog, VirtualHerbalPlant
)
from .serializers import (
    UserSerializer, FarmerProfileSerializer, CustomerProfileSerializer, ProductSerializer, 
    OrderSerializer, OrderItemSerializer, PaymentSerializer, CertificationRequestSerializer, 
    ReviewSerializer, FAQSerializer, ContactFormSerializer, BlogSerializer, VirtualHerbalPlantSerializer
)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class FarmerProfileViewSet(viewsets.ModelViewSet):
    queryset = FarmerProfile.objects.all()
    serializer_class = FarmerProfileSerializer

class CustomerProfileViewSet(viewsets.ModelViewSet):
    queryset = CustomerProfile.objects.all()
    serializer_class = CustomerProfileSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class CertificationRequestViewSet(viewsets.ModelViewSet):
    queryset = CertificationRequest.objects.all()
    serializer_class = CertificationRequestSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

class ContactFormViewSet(viewsets.ModelViewSet):
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormSerializer

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class VirtualHerbalPlantViewSet(viewsets.ModelViewSet):
    queryset = VirtualHerbalPlant.objects.all()
    serializer_class = VirtualHerbalPlantSerializer
