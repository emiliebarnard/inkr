from django.urls import path
from . import views

urlpatterns = [
    path('', views.matchr, name='matchr'),
]