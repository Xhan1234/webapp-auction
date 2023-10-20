from django.contrib import admin
from .models import *

admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('customer', 'vendor', 'product', 'product_title', 'price', 'created_at', 'transaction_id')
    list_filter = ('customer', 'vendor', 'created_at')

admin.site.register(Transaction, TransactionAdmin)
