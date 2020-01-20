from django.apps import AppConfig


class CulturesConfig(AppConfig):
    name = 'Cultures'

    def ready(self):
        from rest_framework import serializers
        from .models import Culture, CultureParameters, Type, NoeudMaitre, NoeudCollecteur, Data
        from datetime import datetime

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
            position='apostiion', topic='sensor/temp', noeudMaitre=master, culture=culture1, status=1)
        collector2 = NoeudCollecteur(
            position='aposition', topic='sensor/temp', noeudMaitre=master, culture=culture2, status=1)

        collector1.save()
        collector2.save()

        collector1.parameters.add(parameter1)
        collector1.parameters.add(parameter2)
        collector2.parameters.add(parameter3)


        data1 = Data(
            value=100, date=datetime(2019,10,15,15,1,14,412), parameter= parameter1, 
            culture=culture1, noeudCollecteur=collector1)
        data2 = Data(
            value=150, date=datetime(2019,10,15,15,1,14), parameter= parameter1, 
            culture=culture1, noeudCollecteur=collector1)
        data3 = Data(
            value=200, date=datetime(2019,10,18,15,1,14), parameter= parameter1, 
            culture=culture1, noeudCollecteur=collector1)
        data4 = Data(
            value=250, date=datetime(2019,10,18,15,1,14), parameter= parameter1, 
            culture=culture1, noeudCollecteur=collector1)
        data5 = Data(
            value=180, date=datetime(2019,10,16,15,1,14), parameter= parameter1, 
            culture=culture1, noeudCollecteur=collector1)
        data6 = Data(
            value=1, date=datetime(2019,10,15,15,1,14), parameter= parameter2, 
            culture=culture1, noeudCollecteur=collector1)
        data7 = Data(
            value=5, date=datetime(2019,10,15,15,1,14), parameter= parameter2, 
            culture=culture1, noeudCollecteur=collector1)
        data8 = Data(
            value=9, date=datetime(2019,10,16,15,1,14), parameter= parameter2, 
            culture=culture1, noeudCollecteur=collector1)
        data9 = Data(
            value=3, date=datetime(2019,10,15,15,1,14), parameter= parameter2, 
            culture=culture1, noeudCollecteur=collector1)
        data10 = Data(
            value=14, date=datetime(2019,10,18,15,1,14), parameter= parameter2, 
            culture=culture1, noeudCollecteur=collector1)

        data1.save()
        data2.save()
        data3.save()
        data4.save()
        data5.save()
        data6.save()
        data7.save()
        data8.save()
        data9.save()
        data10.save()

        print('Parameters saved')
        return super().ready()
