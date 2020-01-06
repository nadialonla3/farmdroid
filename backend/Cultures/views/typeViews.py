from Cultures.models import *
from Cultures.serialisers import *
from rest_framework import generics
from rest_framework.permissions import AllowAny

class ListType(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class= TypeSerializer

    def get_queryset(self):
        return Type.objects.all()

class RetrieveType(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class= TypeSerializer

    def get_queryset(self):
        return Type.objects.all()

class CreateType(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class= TypeSerializer

    def get_queryset(self):
        return Type.objects.all()

class DestroyType(generics.DestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class= TypeSerializer

    def get_queryset(self):
        return Type.objects.all()