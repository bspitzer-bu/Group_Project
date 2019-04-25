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


# def GeneDetailView(request, gene_name):
#     gene = get_object_or_404(models.Gene, gene_name=gene_name)
#     return render(request, 'gene.html', {'gene': gene})

def GeneDetailView(request, id):
    gene = get_object_or_404(models.Gene, id=id)
    return render(request, 'gene.html', {'gene': gene, 'pdbs': models.Gpcr.objects.filter(gene=id)})
