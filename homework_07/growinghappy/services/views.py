from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .models import Service


# Create your views here.

def main_page(request):
    return render(request, 'services/index.html')

class ServiceDetailView (DetailView):
    model = Service

class ServiceListView (ListView):
    model = Service

class ServiceCreateView (CreateView):
    model = Service
    fields = ('name', 'category', 'desc')
    success_url= reverse_lazy('services')

