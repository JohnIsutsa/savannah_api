from django.contrib import admin

from orders.models import Order

# Register your models here.

@admin.register(Order)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ['item', 'amount', 'owner', 'date']
    search_fields = ['item', 'owner__username']
    list_filter = ['date', 'item']
    list_select_related = ['owner']