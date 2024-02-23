from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from authentication.models import User
from authentication.utils import Util
from orders.messages import Message
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
        
        user = User.objects.get(email=self.request.user)
        email = user.email
        phone = user.phone
        
        Util.send_email(
            {
                'email_subject': 'Your Savannah Order Confirmation',
                'email_body': f"Your order for {order_data['amount']} units of {order_data['item']} has been created successfully.",
                'to_email': email
            }
        )
        
        """
        Sends messages using Twilio API
        
        Commented out to make use of cheaper email option.
        Make reference to the messages.py file 
        Requires:
        TWILIO_ACCOUNT_SID 
        TWILIO_AUTH_TOKEN 
        TWILIO_PHONE_NUMBER
        """
        
        # Message.send_message(
        #     {
        #         'body': f"Your order for {order_data['amount']} units of {order_data['item']} has been created successfully.",
        #         'to': phone
        #     }
        # )
    
    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)
    
class OrderDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes=(permissions.IsAuthenticated, IsOwner,)
    lookup_field = 'id'
    
    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)