from .models import *
from .serialisers import *
from rest_framework import generics
from rest_framework.permissions import AllowAny


# ****************************
# * Culture paramter VIEWS   *
# ****************************

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



# ****************************
# * Culture VIEWS            *
# ****************************

class ListCulture(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class= CultureSerializer
    lookup_field='pk'

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



# ****************************
# * DATA VIEWS               *
# ****************************

class RetrieveData(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class= DataSerializer
    lookup_field='pk'
    # filter_class=Data

    def get_queryset(self):
        parameter = self.request.query_params.get('parameter', None)

        queryset= Data.objects.all()
        # queryset=queryset.filter(parameter__name=parameter)
        return queryset

class ListData(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class= DataSerializer

    def get_queryset(self):
        # parameter = self.request.query_params.get('parameter', None)

        # queryset= 
        # queryset=queryset.filter(parameter__name=parameter)
        return Data.objects.all()

class RetrieveDataMean(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class= DataMeanSerializer
    filter_class=DataMean

    def get_queryset(self):
        parameter = self.request.query_params.get('parameter', None)

        queryset= Data.objects.all()
        queryset=queryset.filter(parameter__name=parameter)
        return queryset

class ListDataMean(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class= DataMeanSerializer
    filter_class=DataMean

    def get_queryset(self):
        parameter = self.request.query_params.get('parameter', None)

        queryset= Data.objects.all()
        queryset=queryset.filter(parameter__name=parameter)
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



# ****************************
# * Noeud Collecteur VIEWS   *
# ****************************

class ListNoeudCollecteur(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class= NoeudCollecteurSerializer

    def get_queryset(self):
        return NoeudCollecteur.objects.all()

class RetrieveNoeudCollecteur(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class= NoeudCollecteurSerializer
    lookup_field='pk'

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



# ****************************
# * Noeud Maitre VIEWS       *
# ****************************

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



# ****************************
# * Scheduled Actuator VIEWS *
# ****************************

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



# ****************************
# * TYPE VIEWS               *
# ****************************

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

