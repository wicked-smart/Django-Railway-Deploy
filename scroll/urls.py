from . import views
from django.urls import path


urlpatterns = [
    path("", views.index, name="scroll-index"),
    path("posts", views.posts, name="scroll-posts")
]