from django.urls import path
from . import views



urlpatterns = [
    path('messages/', views.index, name='message'),
    path('send_message/<int:author_id>/<str:product_title>/', views.send_message, name='send_message'),
    path('read_message/<int:chat_id>/', views.read_message, name='read_message'),



]
