from django.shortcuts import render
"""
Need to create three views. 

One view that returns a page for entering in a url to be shortened and possibly a list of enteries

a second view that receives the POST URL, generating a random string, and send the data to the database

a third view that performs the redirecting, don't use HttpResponse


"""
# Create your views here.

def urlItems(request):
    allUrlItems = ToDoItem.objects.all()
    context = {'allurlItems': allUrlItems}
    return render(request, 'shortener_app/index.html', context)


