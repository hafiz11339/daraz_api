from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics
from .models import DarazData
from .serializers import ProductSerializer
# Create your views here.

class MyPageNumberPagination(PageNumberPagination):
    page_size = 50
    page_query_param = 'p'
class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = DarazData.objects.all()
    serializer_class = ProductSerializer

class ProductListAPIView(generics.ListAPIView):
    queryset = DarazData.objects.all()
    serializer_class = ProductSerializer
    pagination_class = MyPageNumberPagination

class ProductCreateAPIView(generics.CreateAPIView):
    queryset = DarazData.objects.all()
    serializer_class = ProductSerializer

