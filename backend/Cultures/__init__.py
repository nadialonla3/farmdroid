from django.apps import AppConfig


class CulturesConfig(AppConfig):
    name = 'Cultures'

    def ready(self):
        return super().ready()

        from rest_framework import serializers
        from .models import Culture, CultureParameters, Type, NoeudMaitre, NoeudCollecteur

        culture1 = Culture(name='corn', scientificName='corn')
        culture2 = Culture(name='corn', scientificName='corn')
        culture1.save()
        culture2.save()

        type1 = Type(name='temp', units='degrees')
        type2 = Type(name='pH', units='none')
        type1.save()
        type2.save()

        parameter1 = CultureParameters(
            name='temperature', minValue=5, maxValue=50, valueType=type1)
        parameter2 = CultureParameters(
            name='pH', minValue=2, maxValue=20, valueType=type2)
        parameter3 = CultureParameters(
            name='temperature', minValue=10, maxValue=40, valueType=type1)
        parameter1.save()
        parameter2.save()
        parameter3.save()

        master = NoeudMaitre(position='aposition', topic='nm1')
        master.save()

        collector1 = NoeudCollecteur(
            position='apostiion', topic='sensor/temp', noeudMaitre=master)
        collector2 = NoeudCollecteur(
            position='aposition', topic='sensor/temp', noeudMaitre=master)
        collector1.save()
        collector2.save()
