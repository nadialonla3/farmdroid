from Cultures.models import *
from Cultures.serialisers import *
from rest_framework import generics
from rest_framework.permissions import AllowAny

class ListActuatorHistory(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class= ActuatorHistorySerializer

    def get_queryset(self):
        return ActuatorHistory.objects.all()

class RetrieveActuatorHistory(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class= ActuatorHistorySerializer

    def get_queryset(self):
        return ActuatorHistory.objects.all()

class CreateActuatorHistory(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class= ActuatorHistorySerializer

    def get_queryset(self):
        return ActuatorHistory.objects.all()

class DestroyActuatorHistory(generics.DestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class= ActuatorHistorySerializer

    def get_queryset(self):
        return ActuatorHistory.objects.all()