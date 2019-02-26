from django.conf.urls import url

from . import views

app_name = 'gpcrdb'

urlpatterns = [
    url('', views.gpcr_list, name='gpcrdb'),
]