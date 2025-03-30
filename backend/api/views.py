from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

def user_status(request):
    return JsonResponse({"message": "User Connected"})
