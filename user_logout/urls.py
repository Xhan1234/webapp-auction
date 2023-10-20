from django.urls import path
from . import views

app_name = 'user_logout'

urlpatterns = [
    # Other URL patterns
    path('', views.user_logout, name='user_logout'),
]
