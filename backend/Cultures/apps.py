from django.apps import AppConfig


class CulturesConfig(AppConfig):
    name = 'Cultures'

    def ready(self):
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
            name='temperature1', minValue=5, maxValue=50, valueType=type1)
        parameter2 = CultureParameters(
            name='pH', minValue=2, maxValue=20, valueType=type2)
        parameter3 = CultureParameters(
            name='temperature2', minValue=10, maxValue=40, valueType=type1)
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

        data1 = Culture(
            value=100, date=(2019,10,15,15,1,14), parameter= parameter1, 
            culture=culture1, noeudCollecteur=collector1)
        data2 = Culture(
            value=150, date=(2019,10,15,15,1,14), parameter= parameter1, 
            culture=culture1, noeudCollecteur=collector1)
        data3 = Culture(
            value=200, date=(2019,10,18,15,1,14), parameter= parameter1, 
            culture=culture1, noeudCollecteur=collector1)
        data4 = Culture(
            value=250, date=(2019,10,18,15,1,14), parameter= parameter1, 
            culture=culture1, noeudCollecteur=collector1)
        data5 = Culture(
            value=180, date=(2019,10,16,15,1,14), parameter= parameter1, 
            culture=culture1, noeudCollecteur=collector1)
        data6 = Culture(
            value=1, date=(2019,10,15,15,1,14), parameter= parameter2, 
            culture=culture1, noeudCollecteur=collector1)
        data7 = Culture(
            value=5, date=(2019,10,15,15,1,14), parameter= parameter2, 
            culture=culture1, noeudCollecteur=collector1)
        data8 = Culture(
            value=9, date=(2019,10,16,15,1,14), parameter= parameter2, 
            culture=culture1, noeudCollecteur=collector1)
        data9 = Culture(
            value=3, date=(2019,10,15,15,1,14), parameter= parameter2, 
            culture=culture1, noeudCollecteur=collector1)
        data10 = Culture(
            value=14, date=(2019,10,18,15,1,14), parameter= parameter2, 
            culture=culture1, noeudCollecteur=collector1)

        print('Parameters saved')
        return super().ready()
