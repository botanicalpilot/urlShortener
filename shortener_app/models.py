import datetime
from django.db import models
from django.utils import timezone


class UrlShortener(models.Model):
    storedURL = models.CharField(max_length = 250)
    # the standInUrl holds the randomly generated id that links to the storedURL
    standInUrl = models.CharField(max_length = 20)
    dateCreated = models.DateField(auto_now_add=True)
    


    def __str__(self):
        return self.storedURL
