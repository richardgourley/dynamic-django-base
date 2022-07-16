from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField

# Create your models here.
class FlatPage(models.Model):
    page_title = models.CharField(max_length=200, unique=True, )
    page_content = HTMLField()
    page_order = models.PositiveIntegerField(default=100)
    slug = models.SlugField(max_length=200, null=False, unique=True)

    def __str__(self):
        return self.page_title

    def get_absolute_url(self):
        return reverse("flatpage_slug", kwargs={"slug":self.slug})
