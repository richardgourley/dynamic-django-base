from django.contrib import admin
from .models import WebsiteSection
from .models import WebsiteSectionCategory

# Register your models here.

class WebsiteSectionCategoryAdmin(admin.ModelAdmin):
    pass

class WebsiteSectionAdmin(admin.ModelAdmin):
    pass

admin.site.register(WebsiteSectionCategory,WebsiteSectionCategoryAdmin)
admin.site.register(WebsiteSection,WebsiteSectionAdmin)