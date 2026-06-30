from rest_framework import viewsets
from .models import SensorEvent
from .serializers import SensorEventSerializer


class SensorEventViewSet(viewsets.ModelViewSet):
    queryset = SensorEvent.objects.all()
    serializer_class = SensorEventSerializer