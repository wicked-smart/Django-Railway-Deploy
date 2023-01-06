from django.urls import path
from django.conf.urls.static import static
from .import views
from mysite import settings


urlpatterns = [
    path('', views.index, name="index")
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)