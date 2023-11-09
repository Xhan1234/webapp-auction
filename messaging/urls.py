from django.urls import path
from . import views

urlpatterns = [
    path('messages/', views.index, name='message'),
    path('messages/inbox/', views.inbox, name='inbox'),
    path('messages/outbox/', views.outbox, name='outbox'),
    path('send_message/<int:author_id>/<str:product_title>/<int:product_id>/', views.send_message, name='send_message'),
    path('read_message/<int:chat_id>/', views.read_message, name='read_message'),

]
