from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Culture)
admin.site.register(Type)
admin.site.register(CultureParameters)
admin.site.register(NoeudMaitre)
admin.site.register(NoeudCollecteur)
admin.site.register(Data)
admin.site.register(ActuatorHistory)
admin.site.register(ScheduledActuators)
