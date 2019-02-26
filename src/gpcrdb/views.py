from django.shortcuts import render

# Create your views here.
from . import models


def gpcr_list(request):
    gpcrs = models.Gpcr.objects.all()
    return render(request, 'gpcr_list.html', {'gpcrs': gpcrs})