from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from orders.models import Order
from orders.serializers import OrderSerializer
from rest_framework import permissions
from orders.permissions import IsOwner

# Create your views here.

class OrderListAPIView(ListCreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes=(permissions.IsAuthenticated,)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)
    
class OrderDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes=(permissions.IsAuthenticated, IsOwner,)
    lookup_field = 'id'
    
    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)