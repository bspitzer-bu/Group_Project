from django.shortcuts import render, get_object_or_404

# Create your views here.
from . import models


def GpcrListView(request):
    gpcrs = models.Gpcr.objects.all()
    return render(request, 'gpcr_list.html', {'gpcrs': gpcrs})


def GpcrDetailView(request, pk):
    gpcr = get_object_or_404(models.Gpcr, pk=pk)
    return render(request, 'gpcr_detail.html', {'gpcr': gpcr})
