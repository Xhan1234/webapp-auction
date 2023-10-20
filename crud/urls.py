from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
path('add-product/', views.add_products, name='add_products'),
path('products/<str:product_slug>/', views.product_detail, name='product_detail'),
path('products/update/<str:product_slug>/', views.update_product, name='update_product'),
path('products/delete/<str:product_slug>/', views.delete_product, name='delete_product'),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)