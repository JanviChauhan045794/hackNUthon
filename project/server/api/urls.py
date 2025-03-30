from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import register_user, LoginView # Ensure these views exist in views.py
from . import views
from api.views import LoginView

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'farmers', views.FarmerProfileViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/register/', register_user, name="register"),
     path("api/login/", LoginView.as_view(), name="login"),   # Use class-based view properly
]
