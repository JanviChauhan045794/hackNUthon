from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet, FarmerProfileViewSet, CustomerProfileViewSet, ProductViewSet, OrderViewSet,
    OrderItemViewSet, PaymentViewSet, CertificationRequestViewSet, ReviewViewSet, FAQViewSet,
    ContactFormViewSet, BlogViewSet, VirtualHerbalPlantViewSet
)

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'farmers', FarmerProfileViewSet)
router.register(r'customers', CustomerProfileViewSet)
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order-items', OrderItemViewSet)
router.register(r'payments', PaymentViewSet)
router.register(r'certification-requests', CertificationRequestViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'faqs', FAQViewSet)
router.register(r'contact-forms', ContactFormViewSet)
router.register(r'blogs', BlogViewSet)
router.register(r'virtual-herbal-plants', VirtualHerbalPlantViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
