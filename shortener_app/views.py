import random, string

from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, reverse, redirect, get_object_or_404
from .models import UrlShortener
"""
Need to create three views. 

One view that returns a page for entering in a url to be shortened and possibly a list of enteries

a second view that receives the POST URL, generating a random string, and send the data to the database

a third view that performs the redirecting, don't use HttpResponse


"""
#This view shows us the index page and a list of urls we have already entered
def urlItems(request):
    allUrlItems = UrlShortener.objects.all()
    context = {'allUrlItems': allUrlItems}
    return render(request, 'shortener_app/index.html', context)

#This view takes the POST url, generates a random string, and saves it to the database
def newUrl(request):
    storedURL = request.POST['storedURL']
    standInUrl = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    context = UrlShortener.objects.create(storedURL = storedURL, standInUrl = standInUrl)
    context.save()
    return redirect('http://127.0.0.1:8000')

#This view performs the redirecting. Do not use HttpResponse
# how do I get the stored url from filtering the database to include only the item with the id
# def redirectUrl(request, UrlShortener_id):
#     return redirect(UrlShortener.objects.filter(standInUrl=UrlShortener_id).values('storedURL'))


# def redirectUrl(request, UrlShortener_id):
#     finalPath = UrlShortener.objects.values_list('storedURL', flat=True).get(standInUrl=UrlShortener_id)
#     return redirect(finalPath.url)

def redirectUrl(request, UrlShortener_id):
    externalUrl = UrlShortener.objects.get(standInUrl=UrlShortener_id)
    return redirect(externalUrl.url)