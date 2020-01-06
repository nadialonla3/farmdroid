from Cultures.models import *
from Cultures.serialisers import *
from rest_framework import generics
from rest_framework.permissions import AllowAny

class ListSensor(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class= SensorSerializer

    def get_queryset(self):
        return Sensor.objects.all()

class RetrieveSensor(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class= SensorSerializer

    def get_queryset(self):
        return Sensor.objects.all()

class CreateSensor(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class= SensorSerializer

    def get_queryset(self):
        return Sensor.objects.all()

class DestroySensor(generics.DestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class= SensorSerializer

    def get_queryset(self):
        return Sensor.objects.all()