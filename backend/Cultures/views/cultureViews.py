from Cultures.models import *
from Cultures.serialisers import *
from rest_framework import generics
from rest_framework.permissions import AllowAny

class ListCulture(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class= CultureSerializer

    def get_queryset(self):
        return Culture.objects.all()

class RetrieveCulture(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class= CultureSerializer

    def get_queryset(self):
        return Culture.objects.all()

class CreateCulture(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class= CultureSerializer

    def get_queryset(self):
        return Culture.objects.all()

class DestroyCulture(generics.DestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class= CultureSerializer

    def get_queryset(self):
        return Culture.objects.all()