from Cultures.models import *
from Cultures.serialisers import *
from rest_framework import generics
from rest_framework.permissions import AllowAny


class ListActuator(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ActuatorSerializer

    def get_queryset(self):
        return Actuator.objects.all()


class RetrieveActuator(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = ActuatorSerializer

    def get_queryset(self):
        return Actuator.objects.all()


class CreateActuator(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = ActuatorSerializer

    def get_queryset(self):
        return Actuator.objects.all()


class DestroyActuator(generics.DestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class = ActuatorSerializer

    def get_queryset(self):
        return Actuator.objects.all()
