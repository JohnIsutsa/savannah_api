from django.urls import path
from orders.views import OrderDetailAPIView, OrderListAPIView


urlpatterns = [
    path('', OrderListAPIView.as_view(), name='order-list'),
    path('<int:id>/', OrderDetailAPIView.as_view(), name='order-detail')
]