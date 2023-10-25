from django.urls import path
from . import views

urlpatterns = [
    path('pusingsarah/', views.pusingsarah, name='pusingsarah'),
]