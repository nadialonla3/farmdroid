from django.db import models


class Type(models.Model):
    name = models.TextField()
    units = models.TextField()

class CultureParameters(models.Model):
    name = models.TextField()
    minValue= models.FloatField()
    maxValue= models.FloatField()
    valueType = models.ForeignKey(to=Type, on_delete=models.SET_NULL, null=True)

class Culture(models.Model):
    name = models.TextField()
    scientificName = models.TextField()
    parameters = models.ManyToManyField(to=CultureParameters)

    def __str__(self):
        return self.name

class NoeudMaitre(models.Model):
    position = models.TextField()
    topic = models.TextField()

class NoeudCollecteur(models.Model):
    position = models.TextField()
    topic = models.TextField()
    noeudMaitre = models.ForeignKey(to=NoeudMaitre, on_delete=models.SET_NULL, null=True, related_name='noeudsCollecteurs')

class Sensor(models.Model):
    gpsCoordinateX= models.FloatField()
    gpsCoordinateY= models.FloatField()
    status=models.IntegerField()
    valueType = models.ForeignKey(to=Type, on_delete=models.SET_NULL, null=True)
    culture = models.ForeignKey(to=Culture, on_delete=models.SET_NULL, null=True, related_name='sensors')
    noeudCollecteur = models.ForeignKey(to=NoeudCollecteur, on_delete=models.SET_NULL, null=True, related_name='sensors')

    def __str__(self):
        return self.status

class Data(models.Model):
    value= models.FloatField()
    date= models.DateTimeField()
    parameter = models.ForeignKey(to=Type, on_delete=models.SET_NULL, null=True)
    culture = models.ForeignKey(to=Culture, on_delete=models.SET_NULL, null=True)
    sensor = models.ForeignKey(to=Sensor, on_delete=models.SET_NULL, null=True)

class DataMean(models.Model):
    value= models.FloatField()
    date= models.DateTimeField()
    valueType = models.ForeignKey(to=Type, on_delete=models.SET_NULL, null=True)
    culture = models.ForeignKey(to=Culture, on_delete=models.SET_NULL, null=True)

class Actuator(models.Model):
    name = models.TextField()
    gpsCoordinateX= models.FloatField()
    gpsCoordinateY= models.FloatField()
    status=models.IntegerField()
    valueType = models.TextField()
    noeudCollecteur = models.ForeignKey(to=NoeudCollecteur, on_delete=models.SET_NULL, null=True, related_name='actuators')

class ActuatorHistory(models.Model):
    date= models.DateTimeField()
    Actuator = models.ForeignKey(to=Actuator, on_delete=models.SET_NULL, null=True, related_name='history')

class ScheduledActuators(models.Model):
    date= models.DateTimeField()
    repeatInterval=models.IntegerField()
    timestamp = models.DateTimeField()
    actuator = models.ForeignKey(to=Actuator, on_delete=models.SET_NULL, null=True, related_name='scheduled')
