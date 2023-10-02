from django.urls import path
from task.views import index
from . import views

urlpatterns = [
    path("", views.index, name="index"),
]