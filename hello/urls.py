from django.urls import path
from django.conf.urls.static import static
from .import views
from mysite import settings


urlpatterns = [
    path('', views.index, name="index"),
    path('<int:flight_id>/', views.detail, name="flight_detail"),
    path('<int:flight_id>/book', views.book, name="book")
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)