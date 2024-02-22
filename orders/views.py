from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from authentication.models import User
from authentication.utils import Util
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
        order_data = serializer.data
        
        Util.send_email(
            {
                'email_subject': 'Your Savannah Order Confirmation',
                'email_body': f"Your order for {order_data['amount']} units of {order_data['item']} has been created successfully.",
                'to_email': self.request.user
            }
        )
    
    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)
    
class OrderDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes=(permissions.IsAuthenticated, IsOwner,)
    lookup_field = 'id'
    
    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)