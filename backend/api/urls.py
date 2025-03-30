from django.urls import path
from .views import user_status

urlpatterns = [
    path('user-status/', user_status),
]
