from django.shortcuts import render
from django.views import generic
from .models import FlatPage

# Create your views here.
class FlatPageDetailView(generic.DetailView):
    model = FlatPage
    template_name = 'flatpages/template.html'