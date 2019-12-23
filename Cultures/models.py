from django.db import models

class Culture(models.Model):
    name = models.TextField()
    scientificName = models.TextField()

    def __str__(self):
        return self.name

class Type(models.Model):
    name = models.TextField()
    units = models.TextField()

class CultureParameters(models.Model):
    name = models.TextField()
    minValue= models.FloatField()
    maxValue= models.FloatField()
    culture = models.ForeignKey(to=Culture, on_delete=models.SET_NULL, null=True)
    type = models.ForeignKey(to=Type, on_delete=models.SET_NULL, null=True)

class ParamAttribution(models.Model):
    culture = models.ForeignKey(to=Culture, on_delete=models.SET_NULL, null=True)
    cultureParameters = models.ForeignKey(to=CultureParameters, on_delete=models.SET_NULL, null=True)

class NoeudMaitre(models.Model):
    position = models.TextField()

class NoeudCollecteur(models.Model):
    position = models.TextField()
    noeudMaitre = models.ForeignKey(to=NoeudMaitre, on_delete=models.SET_NULL, null=True)

class Sensor(models.Model):
    gpsCoordinateX= models.FloatField()
    gpsCoordinateY= models.FloatField()
    status=models.IntegerField()
    Type = models.ForeignKey(to=Type, on_delete=models.SET_NULL, null=True)
    culture = models.ForeignKey(to=Culture, on_delete=models.SET_NULL, null=True)
    noeudCollecteur = models.ForeignKey(to=NoeudCollecteur, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.status

class Data(models.Model):
    value= models.FloatField()
    date= models.DateTimeField()
    type = models.ForeignKey(to=Type, on_delete=models.SET_NULL, null=True)
    culture = models.ForeignKey(to=Culture, on_delete=models.SET_NULL, null=True)
    sensor = models.ForeignKey(to=Sensor, on_delete=models.SET_NULL, null=True)

class Actuator(models.Model):
    name = models.TextField()
    gpsCoordinateX= models.FloatField()
    gpsCoordinateY= models.FloatField()
    status=models.IntegerField()
    type = models.TextField()
    NoeudCollecteur = models.ForeignKey(to=NoeudCollecteur, on_delete=models.SET_NULL, null=True)

class ActuatorHistory(models.Model):
    date= models.DateTimeField()
    Actuator = models.ForeignKey(to=Actuator, on_delete=models.SET_NULL, null=True)

class ScheduledActuators(models.Model):
    date= models.DateTimeField()
    repeatInterval=models.IntegerField()
    Timestamp = models.DateTimeField()
    Actuator = models.ForeignKey(to=Actuator, on_delete=models.SET_NULL, null=True)