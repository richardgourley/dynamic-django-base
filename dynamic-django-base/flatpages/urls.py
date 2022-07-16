from django.urls import path
from .views import FlatPageDetailView, FlatPageCategory

app_name = 'flatpages'
urlpatterns = [
    path('<slug:slug>', FlatPageDetailView.as_view(), name="flatpage_detail"),
]
