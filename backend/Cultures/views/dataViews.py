from Cultures.models import *
from Cultures.serialisers import *
from rest_framework import generics
from rest_framework.permissions import AllowAny

class RetrieveData(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class= DataSerializer
    filter_class=Data

    def get_queryset(self):
        parameter = self.request.query_params.get('parameter', None)

        queryset= Data.objects.all()
        queryset=queryset.filter(type__name=parameter)
        return queryset

class ListData(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class= DataSerializer

    def get_queryset(self):
        parameter = self.request.query_params.get('parameter', None)

        queryset= Data.objects.all()
        queryset=queryset.filter(type__name=parameter)
        return queryset

class RetrieveDataMean(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class= DataMeanSerializer
    filter_class=DataMean

    def get_queryset(self):
        parameter = self.request.query_params.get('parameter', None)

        queryset= Data.objects.all()
        queryset=queryset.filter(type__name=parameter)
        return queryset

class ListDataMean(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class= DataMeanSerializer
    filter_class=DataMean

    def get_queryset(self):
        parameter = self.request.query_params.get('parameter', None)

        queryset= Data.objects.all()
        queryset=queryset.filter(type__name=parameter)
        return queryset

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