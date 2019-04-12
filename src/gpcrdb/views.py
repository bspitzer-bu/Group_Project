from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core import serializers
from django.views.generic import ListView


# Create your views here.
from . import models


def GpcrDetailView(request, pk):
    gpcr = get_object_or_404(models.Gpcr, pk=pk)
    return render(request, 'gpcr_detail.html', {'gpcr': gpcr})

def GpcrListView_asJson(request):
    object_list = models.Gpcr.objects.all() #or any kind of queryset
    json = serializers.serialize('json', object_list)
    return HttpResponse(json, content_type='application/json')


def GpcrListView(request):
    return render(request, 'gpcr_list.html', {})

def GpcrTreeView(request):
    return render(request, 'tree.html', {})
