from django.conf.urls import url

from . import views

app_name = 'gpcrdb'

urlpatterns = [
    url(r'^$', views.GpcrListView, name='gpcrdb'),
    url(r'(?P<pk>\d+)/$', views.GpcrDetailView, name='gpcr_detail'),
]
