from django.db import models

# Create your models here.

class WebsiteSectionCategory(models.Model):
    section_category_title = models.CharField(max_length=200, unique=True, help_text="Add a category title for each website section to appear under.")
    section_category_image = models.ImageField(upload_to="images", null=True, blank=True)

    class Meta():
        verbose_name_plural = "Website section categories"

    def __str__(self):
        return self.section_category_title

class WebsiteSection(models.Model):
    section_title = models.CharField(max_length=200, unique=True, help_text="Add a title for the website section.")
    section_image = models.ImageField(upload_to="images", null=True, blank=True)
    section_main_text = models.TextField(null=False, blank=False)
    section_django_url = models.CharField(max_length=100, unique=True, help_text="Full URL NOT REQUIRED - just enter the extended url you want to link to eg. /calculators/home")
    section_order = models.PositiveSmallIntegerField(default=100)
    section_category = models.ForeignKey(WebsiteSectionCategory, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.section_title
