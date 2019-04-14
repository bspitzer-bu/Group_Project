from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core import serializers


# Create your views here.
from . import models


def GpcrDetailView(request, pdb_id):
    gpcr = get_object_or_404(models.Gpcr, pdb_id=pdb_id)
    return render(request, 'gpcr_detail.html', {'gpcr': gpcr})



def GpcrListView_asJson(request):
    object_list = models.Gpcr.objects.all() #or any kind of queryset
    json = serializers.serialize('json', object_list)
    return HttpResponse(json, content_type='application/json')


def GpcrListView(request):
    return render(request, 'gpcr_list.html', {})

def GpcrTreeView(request):
    return render(request, 'tree.html', {})


from tablib import Dataset
from .resources import GpcrResource

def simple_upload(request):
    if request.method == 'POST':
        gpcr_resource = GpcrResource()
        dataset = Dataset()
        new_gpcrs = request.FILES['myfile']
        # dataset.load(new_gpcrs.read().decode('utf-8'), format='csv')
        imported_data = dataset.load(new_gpcrs.read().decode('utf-8'), format='csv')
        result = gpcr_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            gpcr_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'core/simple_upload.html')
