from django.contrib import admin
from django.urls import path, include
from todo.views import homepage, test
from django.conf import settings
from django.conf.urls.static import static
from todo.views import homepage
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('todo.urls'))


]
