from Cultures.models import *
from Cultures.serialisers import *
from rest_framework import generics
from rest_framework.permissions import AllowAny

class ListCultureParameters(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class= CultureParametersSerializer

    def get_queryset(self):
        return CultureParameters.objects.all()

class RetrieveCultureParameters(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class= CultureParametersSerializer

    def get_queryset(self):
        return CultureParameters.objects.all()

class CreateCultureParameters(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class= CultureParametersSerializer

    def get_queryset(self):
        return CultureParameters.objects.all()

class DestroyCultureParameters(generics.DestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class= CultureParametersSerializer

    def get_queryset(self):
        return CultureParameters.objects.all()