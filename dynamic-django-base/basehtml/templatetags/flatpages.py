from django import template
from flatpages.models import FlatPage

register = template.Library()

@register.simple_tag
def get_flatpages():
	flatpages = FlatPage.objects.all().order_by('page_order')
	return flatpages