from Cultures.models import *
from Cultures.serialisers import *
from rest_framework import generics
from rest_framework.permissions import AllowAny

class ListNoeudCollecteur(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class= NoeudCollecteurSerializer

    def get_queryset(self):
        return NoeudCollecteur.objects.all()

class RetrieveNoeudCollecteur(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class= NoeudCollecteurSerializer

    def get_queryset(self):
        return NoeudCollecteur.objects.all()

class CreateNoeudCollecteur(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class= NoeudCollecteurSerializer

    def get_queryset(self):
        return NoeudCollecteur.objects.all()

class DestroyNoeudCollecteur(generics.DestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class= NoeudCollecteurSerializer

    def get_queryset(self):
        return NoeudCollecteur.objects.all()