from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'gpcrdb'

urlpatterns = [
    url(r'(?P<pk>\d+)/$', views.GpcrDetailView, name='gpcr_detail'),
    path('', views.GPCRList.as_view(), name='gpcrdb'),
]
