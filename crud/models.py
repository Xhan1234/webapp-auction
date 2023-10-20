from django.db import models
from django.utils import timezone
from autoslug import AutoSlugField
from user_registration.models import UserProfile

class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    STATUS_CHOICES = [
        (True, 'Active'),
        (False, 'Sold'),
    ]
    title = models.CharField(max_length=200, null=False , blank=False)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    description = models.TextField(max_length=400, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,  blank=False)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    quantity = models.PositiveIntegerField(default=1, null=True, blank=True,)
    status = models.BooleanField(default=True, choices=STATUS_CHOICES)

    # Replace the previous slug field with AutoSlugField
    slug = AutoSlugField(populate_from='title', unique=True)  # Populate from 'title' and ensure uniqueness

    def __str__(self):
        return self.title