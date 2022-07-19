from django import template
from websitesections.models import WebsiteSectionCategory

register = template.Library()

@register.simple_tag
def get_website_section_categories():
	website_section_categories = WebsiteSectionCategory.objects.all().order_by('section_category_title')
	return website_section_categories