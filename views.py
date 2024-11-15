# views.py
from django.shortcuts import render
from db.models import Product

def home(request):
    return render(request, 'home.html')

def scan_product(request):
    product_details = None
    error_message = None
    
    if request.method == 'POST':
        # Get the UPC code from the form input
        upc_code = request.POST.get('upc_code')
        
        try:
            # Search for the product by UPC code
            product = Product.objects.get(upc_code=upc_code)
            product_details = {
                'name': product.name,
                'price': product.price,
            }
        except Product.DoesNotExist:
            error_message = 'Product not found. Please check the UPC code.'

    return render(request, 'scan_product.html', {'product_details': product_details, 'error_message': error_message})
