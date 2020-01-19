from django.urls import path
from django.conf.urls import url, include
from .views.dataViews import *
from django.views.generic.base import TemplateView

urlpatterns = [
    path("cultures/data/<parameter>/<int:pk>" , RetrieveData.as_view(), name='post-rud'),
    path("cultures/dataMean/<parameter>/<int:pk>" , RetrieveDataMean.as_view(), name='post-rud'),
    path("cultures/dataMean/<parameter>/<date1>/<date2>" , ListDataMean.as_view(), name='post-rud'),
    path("cultures/data/<parameter>/<date1>/<date2>" , ListData.as_view(), name='post-rud'),
]
