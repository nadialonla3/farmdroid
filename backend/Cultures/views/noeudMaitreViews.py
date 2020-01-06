from Cultures.models import *
from Cultures.serialisers import *
from rest_framework import generics
from rest_framework.permissions import AllowAny

class ListNoeudMaitre(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class= NoeudMaitreSerializer

    def get_queryset(self):
        return NoeudMaitre.objects.all()

class RetrieveNoeudMaitre(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class= NoeudMaitreSerializer

    def get_queryset(self):
        return NoeudMaitre.objects.all()

class CreateNoeudMaitre(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class= NoeudMaitreSerializer

    def get_queryset(self):
        return NoeudMaitre.objects.all()

class DestroyNoeudMaitre(generics.DestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class= NoeudMaitreSerializer

    def get_queryset(self):
        return NoeudMaitre.objects.all()