from django.urls import path
from django.conf.urls import url, include
from .views import *
from django.views.generic.base import TemplateView

urlpatterns = [
    path("cultures/data1/<int:pk>",
         RetrieveData.as_view(), name='post-rud'),
    path("cultures/dataMean/<int : parameter>/<int:pk>",
         RetrieveDataMean.as_view(), name='post-rud'),
    path("cultures/dataMean/<int : parameter>",
         ListDataMean.as_view(), name='post-rud'),
    path("cultures/data",
         ListData.as_view(), name='data'),
     
     path("cultures/noeudMaitre", 
          ListNoeudMaitre.as_view(), name='masternode'),
]
# /<int:pk>