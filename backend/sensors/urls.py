from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SensorEventViewSet

router = DefaultRouter()
router.register(r'sensors', SensorEventViewSet)

urlpatterns = [
    path('', include(router.urls)),
]