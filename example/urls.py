from django.urls import path
from . import views

urlpatterns = [
    path("", views.exampleHome, name="example-home"),
]
