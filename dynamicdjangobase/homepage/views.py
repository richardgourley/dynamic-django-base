from django.shortcuts import render
from websitesections.models import WebsiteSection

# Create your views here.
def index(request):
    website_sections = WebsiteSection.objects.all().order_by('section_order')
    return render(request, 'homepage/index.html', {"website_sections":website_sections})
