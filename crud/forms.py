from django.forms import ModelForm
from .models import *

class CreateProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = ['author', 'created_at', 'status']