from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("cafes/", include("cafes.urls")),
    path("admin/", admin.site.urls),
]
