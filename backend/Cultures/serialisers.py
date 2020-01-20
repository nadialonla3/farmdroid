from rest_framework import serializers
from .models import *


class CultureSerializer(serializers.ModelSerializer):
    parameters = serializers.StringRelatedField(many=True)

    class Meta:
        model = Culture
        fields = ['name', 'scientificName', 'parameters']


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['name', 'units']


class CultureParametersSerializer(serializers.ModelSerializer):
    valueType = TypeSerializer()
    culture = CultureSerializer()

    class Meta:
        model = CultureParameters
        fields = ['name', 'minValue', 'maxValue', 'valueType']


class NoeudMaitreSerializer(serializers.ModelSerializer):
    noeudCollecteurs = serializers.StringRelatedField(many=True)

    class Meta:
        model = NoeudMaitre
        fields = ['position', 'topic', 'noeudCollecteurs']


class NoeudCollecteurSerializer(serializers.ModelSerializer):
    noeudMaitre = serializers.StringRelatedField()
    actuators = serializers.StringRelatedField(many=True)
    parameters = CultureParametersSerializer(many=True, read_only=True)
    culture = serializers.StringRelatedField()

    class Meta:
        model = NoeudCollecteur
        fields = ['position', 'topic', 'noeudMaitre', 'status', 'culture', 'parameters' ]


class DataSerializer(serializers.ModelSerializer):
    valueType = TypeSerializer()
    culture = serializers.StringRelatedField()
    noeudCollecteur = serializers.StringRelatedField()
    class Meta:
        model = Data
        fields = ['value', 'date', 'valueType', 'culture', 'noeudCollecteur']

class DataMeanSerializer(serializers.ModelSerializer):
    valueType = TypeSerializer()
    culture = serializers.StringRelatedField()
    class Meta:
        model = Data
        fields = ['value', 'date', 'valueType', 'culture']


class ActuatorHistorySerializer(serializers.ModelSerializer):
    noeudCollecteur = serializers.StringRelatedField()
    class Meta:
        model = ActuatorHistory
        fields = ['date', 'action', 'noeudCollecteur']

class ScheduledActuatorsSerializer(serializers.ModelSerializer):
    noeudCollecteur = serializers.StringRelatedField()
    class Meta:
        model = ScheduledActuators
        fields = ['date', 'repeatInterval', 'timestamp', 'action', 'noeudCollecteur']