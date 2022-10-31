from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band, Title


def hello(request):
    bands = Band.objects.all()
    return render(request, "listings/hello.html", {"bands": bands})


def about(request):
    return HttpResponse("<h1> About Us</h1> <p> We love merch!</p>")
