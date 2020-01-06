from Cultures.models import *
from Cultures.serialisers import *
from rest_framework import generics
from rest_framework.permissions import AllowAny

class ListScheduledActuators(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class= ScheduledActuatorsSerializer

    def get_queryset(self):
        return ScheduledActuators.objects.all()

class RetrieveScheduledActuators(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class= ScheduledActuatorsSerializer

    def get_queryset(self):
        return ScheduledActuators.objects.all()

class CreateScheduledActuators(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class= ScheduledActuatorsSerializer

    def get_queryset(self):
        return ScheduledActuators.objects.all()

class DestroyScheduledActuators(generics.DestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class= ScheduledActuatorsSerializer

    def get_queryset(self):
        return ScheduledActuators.objects.all()