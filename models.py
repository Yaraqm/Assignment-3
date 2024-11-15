import sys
from django.db import models

try:
    from django.db import models
except Exception:
    print('Exception: Django Not Found, please install it with "pip install django".')
    sys.exit()

# User model for demonstration purposes
class User(models.Model):
    name = models.CharField(max_length=50, default="Dan")

    def __str__(self):
        return self.name

# Product model for the cash register
class Product(models.Model):
    upc_code = models.CharField(max_length=12, unique=True)  
    name = models.CharField(max_length=100) 
    price = models.DecimalField(max_digits=10, decimal_places=2) 

    def __str__(self):
        return f"{self.name} ({self.upc_code}): ${self.price}"
