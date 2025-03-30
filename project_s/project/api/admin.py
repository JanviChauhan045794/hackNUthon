from django.contrib import admin
from .models import (
    User, FarmerProfile, CustomerProfile, Product, Order, OrderItem, Payment,
    CertificationRequest, Review, FAQ, ContactForm, Blog, VirtualHerbalPlant
)

admin.site.register(User)
admin.site.register(FarmerProfile)
admin.site.register(CustomerProfile)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Payment)
admin.site.register(CertificationRequest)
admin.site.register(Review)
admin.site.register(FAQ)
admin.site.register(ContactForm)
admin.site.register(Blog)
admin.site.register(VirtualHerbalPlant)
