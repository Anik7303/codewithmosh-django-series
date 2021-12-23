from django.urls import path
from . import views

urlpatterns = [path("", views.index, name="playground_index")]
