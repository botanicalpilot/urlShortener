
from django.urls import path

from . import views

app_name = 'shortener_app'
urlpatterns = [
    path('', views.allUrlItems, name='allUrlItems'),
]