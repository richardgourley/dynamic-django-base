from django import template

register = template.Library()

@register.simple_tag
def get_copyright_details():
	return {
		"start_year":None,
		"company_name":"Your website name goes here",
	}


