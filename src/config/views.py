from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.generic import View, TemplateView

class HomeView(TemplateView):
    template_name = 'home.html'

def ContactView(request):
    return render(request, 'contact.html')

def UsageView(request):
    return render(request, 'usage.html')
