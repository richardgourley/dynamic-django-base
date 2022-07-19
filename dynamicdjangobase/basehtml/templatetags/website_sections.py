from django import template
from websitesections.models import WebsiteSection

register = template.Library()

@register.simple_tag
def get_website_sections():
	website_sections = WebsiteSection.objects.all().order_by('section_order')
	return website_sections