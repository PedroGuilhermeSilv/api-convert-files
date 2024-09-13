
from django.contrib import admin
from django.urls import path

from src.infra.convert.routers.controllers import api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
]
