from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
]
