from django.urls import path
from .import views
from todo.views import homepage, test
from django.conf import settings
from django.conf.urls.static import static
from todo.views import homepage
from django.conf import settings

urlpatterns = [
    path("", views.test, name="test"),
    path("", views.homepage, name="home"),


]   + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
