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
    sensors = serializers.StringRelatedField(many=True)
    actuators = serializers.StringRelatedField(many=True)
    class Meta:
        model = NoeudCollecteur
        fields = ['position', 'topic', 'noeudMaitre', 'sensors', 'actuators']


class SensorSerializer(serializers.ModelSerializer):
    valueTtype = TypeSerializer()
    culture = CultureSerializer()
    noeudCollecteur = serializers.StringRelatedField()
    class Meta:
        model = Sensor
        fields = ['gpsCoordinateX', 'gpsCoordinateY',
                  'status', 'valueType', 'culture', 'noeudCollecteur']

class DataSerializer(serializers.ModelSerializer):
    valueType = TypeSerializer()
    culture = serializers.StringRelatedField()
    sensor = serializers.StringRelatedField()
    class Meta:
        model = Data
        fields = ['value', 'date', 'valueType', 'culture', 'sensor']

class DataMeanSerializer(serializers.ModelSerializer):
    valueType = TypeSerializer()
    culture = serializers.StringRelatedField()
    class Meta:
        model = Data
        fields = ['value', 'date', 'valueType', 'culture']

class ActuatorSerializer(serializers.ModelSerializer):
    valueType = TypeSerializer()
    noeudCollecteur = serializers.StringRelatedField()
    history = serializers.StringRelatedField(many=True)
    scheduled = serializers.StringRelatedField(many=True)

    class Meta:
        model = Actuator
        fields = ['name', 'gpsCoordinateX', 'gpsCoordinateY', 'status', 'valueType', 'noeudCollecteur', 'history']

class ActuatorHistorySerializer(serializers.ModelSerializer):
    actuator = serializers.StringRelatedField()
    class Meta:
        model = ActuatorHistory
        fields = ['date', 'actuator']

class ScheduledActuatorSerializer(serializers.ModelSerializer):
    actuator = serializers.StringRelatedField()
    class Meta:
        model = ScheduledActuators
        fields = ['date', 'repeatInterval', 'timestamp', 'actuator']