"""
views
"""

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .models import Service

# Create your views here.

def main_page(request):
    """
    main_page
    """
    return render(request, 'services/index.html')

class ServiceDetailView (DetailView):
    """
    ServiceDetailView
    """
    model = Service


class ServiceListView (ListView):
    """
    ServiceListView
    """
    model = Service

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['help_text'] = 'хэлптекст'
        return context


class ServiceCreateView (CreateView):
    """
    ServiceCreateView
    """
    model = Service
    fields = ('name','category','desc')
    success_url = reverse_lazy('services')
