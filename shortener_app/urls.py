
from django.urls import path

from .import views

app_name = 'shortener_app'
urlpatterns = [
    path('', views.urlItems, name='urlItems'),
    path('newUrl', views.newUrl, name='newUrl'),
    path('redirectUrl/<slug:UrlShortener_id>/', views.redirectUrl, name='redirectUrl'),
]