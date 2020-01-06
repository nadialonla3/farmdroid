from Cultures.models import *
from Cultures.serialisers import *
from rest_framework import generics
from rest_framework.permissions import AllowAny

class ListParamAttribution(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class= ParamAttributionSerializer

    def get_queryset(self):
        return ParamAttribution.objects.all()

class RetrieveParamAttribution(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class= ParamAttributionSerializer

    def get_queryset(self):
        return ParamAttribution.objects.all()

class CreateParamAttribution(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class= ParamAttributionSerializer

    def get_queryset(self):
        return ParamAttribution.objects.all()

class DestroyParamAttribution(generics.DestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class= ParamAttributionSerializer

    def get_queryset(self):
        return ParamAttribution.objects.all()