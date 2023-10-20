from django.urls import path
from . import views

app_name = 'vendor_user_profile'

urlpatterns = [
path('<str:username>/', views.public_profile, name='public_profile'),
path('account/<str:username>/', views.personal_profile, name='personal_profile'),
path('<str:username>/edit-profile/', views.edit_profile, name='edit_profile'),



]