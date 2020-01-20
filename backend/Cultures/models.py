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
    parameters = models.ManyToManyField(to=CultureParameters)
    status = models.IntegerField()
    culture = models.ForeignKey(to=Culture, on_delete=models.SET_NULL, null=True, related_name='noeudCollecteurs')


class Data(models.Model):
    value= models.FloatField()
    date= models.DateTimeField()
    parameter = models.ForeignKey(to=Type, on_delete=models.SET_NULL, null=True)
    culture = models.ForeignKey(to=Culture, on_delete=models.SET_NULL, null=True)
    noeudCollecteur = models.ForeignKey(to=NoeudCollecteur, on_delete=models.SET_NULL, null=True)

class DataMean(models.Model):
    value= models.FloatField()
    date= models.DateTimeField()
    valueType = models.ForeignKey(to=Type, on_delete=models.SET_NULL, null=True)
    culture = models.ForeignKey(to=Culture, on_delete=models.SET_NULL, null=True)

class ActuatorHistory(models.Model):
    date= models.DateTimeField()
    noeudCollecteur = models.ForeignKey(to=NoeudCollecteur, on_delete=models.SET_NULL, null=True, related_name='actuatorHistory')
    action = models.TextField()

class ScheduledActuators(models.Model):
    date= models.DateTimeField()
    repeatInterval=models.IntegerField()
    timestamp = models.DateTimeField()
    noeudCollecteur = models.ForeignKey(to=NoeudCollecteur, on_delete=models.SET_NULL, null=True, related_name='actuatorSchedule')
    action = models.TextField()
