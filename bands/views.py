from bands import models
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

def bands(request):
    bands = models.Band.objects.all()
    return render(request, 'bands/band_listing.html', {'bands': bands})
    