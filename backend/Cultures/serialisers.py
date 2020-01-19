from rest_framework import serializers
from .models import *


class CultureSerializer(serializers.ModelSerializer):
    parameters = serializers.StringRelatedField(many=True)
    sensors = serializers.StringRelatedField(many=True)

    class Meta:
        model = Culture
        fields = ['name', 'scientificName', 'parameters', 'sensors']


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['name', 'units']


class CultureParametersSerializer(serializers.ModelSerializer):
    type = TypeSerializer()

    class Meta:
        model = CultureParameters
        fields = ['name', 'minValue', 'maxValue', 'type']


class NoeudMaitreSerializer(serializers.ModelSerializer):
    noeudCollecteurs = serializers.StringRelatedField(many=True)

    class Meta:
        model = NoeudMaitre
        fields = ['position', 'noeudCollecteurs']


class NoeudCollecteurSerializer(serializers.ModelSerializer):
    noeudMaitre = serializers.StringRelatedField()
    sensors = serializers.StringRelatedField(many=True)
    actuators = serializers.StringRelatedField(many=True)
    class Meta:
        model = NoeudCollecteur
        fields = ['position', 'noeudMaitre', 'sensors', 'actuators']


class SensorSerializer(serializers.ModelSerializer):
    type = TypeSerializer()
    culture = CultureSerializer()
    noeudCollecteur = serializers.StringRelatedField()
    class Meta:
        model = Sensor
        fields = ['gpsCoordinateX', 'gpsCoordinateY',
                  'status', 'type', 'culture', 'noeudCollecteur']

class DataSerializer(serializers.ModelSerializer):
    type = TypeSerializer()
    culture = serializers.StringRelatedField()
    sensor = serializers.StringRelatedField()
    class Meta:
        model = Data
        fields = ['value', 'date', 'type', 'culture', 'sensor']

class DataMeanSerializer(serializers.ModelSerializer):
    type = TypeSerializer()
    culture = serializers.StringRelatedField()
    class Meta:
        model = Data
        fields = ['value', 'date', 'type', 'culture']

class ActuatorSerializer(serializers.ModelSerializer):
    type = TypeSerializer()
    noeudCollecteur = serializers.StringRelatedField()
    history = serializers.StringRelatedField(many=True)
    scheduled = serializers.StringRelatedField(many=True)

    class Meta:
        model = Actuator
        fields = ['name', 'gpsCoordinateX', 'gpsCoordinateY', 'status', 'type', 'noeudCollecteur', 'history']

class ActuatorHistorySerializer(serializers.ModelSerializer):
    actuator = serializers.StringRelatedField()
    class Meta:
        model = ActuatorHistory
        fields = ['date', 'actuator']

class ScheduledActuators(serializers.ModelSerializer):
    actuator = serializers.StringRelatedField()
    class Meta:
        model = ScheduledActuators
        fields = ['date', 'repeatInterval', 'timestamp', 'actuator']