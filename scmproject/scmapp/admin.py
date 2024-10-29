from django.contrib import admin

from .models import Admin, Supplier,Registration,Product,Customer,Order,Seller

# Register your models here.
admin.site.register(Admin)
admin.site.register(Supplier)
admin.site.register(Registration)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Seller)