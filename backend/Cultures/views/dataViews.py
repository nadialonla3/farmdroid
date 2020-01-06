from Cultures.models import *
from Cultures.serialisers import *
from rest_framework import generics
from rest_framework.permissions import AllowAny

class ListData(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class= DataSerializer

    def get_queryset(self):
        return Data.objects.all()

class RetrieveData(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class= DataSerializer

    def get_queryset(self):
        return Data.objects.all()

class CreateData(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class= DataSerializer

    def get_queryset(self):
        return Data.objects.all()

class DestroyData(generics.DestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class= DataSerializer

    def get_queryset(self):
        return Data.objects.all()