from django.contrib import admin
from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'author_name')
    list_filter = ('status', 'author')# Define the fields to display in the admin list view

    def author_name(self, obj):
        return obj.author.business_name  # Replace 'business_name' with the actual field name in the UserProfile model that stores the author's name

    author_name.short_description = 'Author'  # Set a custom column header for the author's name

admin.site.register(Product, ProductAdmin)  # Register the Product model with the custom admin class