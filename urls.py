from django.contrib import admin
from django.urls import path
from db import views 

# Add the new home route to the URL patterns
urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('scan/', views.scan_product, name='scan_product'),
]
