from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'gpcrdb'

urlpatterns = [
    path('', views.GpcrListView, name='gpcrdb'),
    url('tree/', views.GpcrTreeView, name='tree'),
    url(r'^json/$', views.GpcrListView_asJson, name='json'),
    path('<str:pdb_id>/', views.GpcrDetailView, name='gpcr-detail'),
    path('gene/<str:gene_name>/', views.GeneDetailView, name='gene-detail'),

]
