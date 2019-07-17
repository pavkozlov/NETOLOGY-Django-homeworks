from django.urls import path
from .views import stations_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('stations/', stations_view, name='stations_view')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
