############################################################################
## Django ORM Standalone Python Template
############################################################################

# Turn off bytecode generation
import sys
sys.dont_write_bytecode = True

# Django specific settings
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
import django
django.setup()

# Import your models for use in your script
from db.models import Product

############################################################################
## START OF APPLICATION
############################################################################

# Seed a few products into the database if the table is empty
if Product.objects.count() == 0:
    Product.objects.create(upc_code="12345", name="Coffee", price=8.32)
    Product.objects.create(upc_code="23456", name="Tea", price=4.99)
    Product.objects.create(upc_code="34567", name="Sandwich", price=5.50)

print("Products seeded in the database:")
for p in Product.objects.all():
    print(f"UPC: {p.upc_code} \tName: {p.name} \tPrice: ${p.price}")

# Simulate product scanning (via input box)
upc_input = input("\nEnter UPC code to scan product: ")

# Look up the product by UPC code
try:
    product = Product.objects.get(upc_code=upc_input)
    print(f"Product Scanned: {product.name}, Price: ${product.price}")
except Product.DoesNotExist:
    print("Product not found. Please check the UPC code.")
