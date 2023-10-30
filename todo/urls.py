from django.urls import path
from .import views
from todo.views import *
from django.conf import settings
from django.conf.urls.static import static
from todo.views import homepage
from django.conf import settings

urlpatterns = [
    path("", views.test, name="test"),
    path("", views.homepage, name="home"),
    path("add-todo/", add_todo, name="add-todo"),
    path("delete-todo/<id>/", delete_todo, name="delete-todo"),

]   + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
