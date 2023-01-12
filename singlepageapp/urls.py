from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="singleapp-index"),
    path("section/<int:section_id>", views.section, name="singlepageapp-section")
]