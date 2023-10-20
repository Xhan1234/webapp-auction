from django.urls import path
from . import views

app_name = 'order_product'

urlpatterns = [


    path('shopping-cart/<int:product_id>/', views.add_cart, name='add_cart'),
    path('cart/', views.cart, name='cart'),
    path('cart/delete/<int:cart_item_id>/', views.delete_cart_item, name='delete_cart_item'),
    path('make_purchase/', views.make_purchase, name='make_purchase'),
    path('checkout/', views.checkout, name='checkout'),
    path('order/generate_invoice_pdf/', views.generate_invoice_pdf, name='generate_invoice_pdf'),



]
