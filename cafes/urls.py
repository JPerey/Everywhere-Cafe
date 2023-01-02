from django.urls import path
from . import views

urlpatterns = [
    path("", views.cafes, name="cafes"),
]
