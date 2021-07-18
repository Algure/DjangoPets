from django.shortcuts import render
from django.http import HttpResponse

from .models import Pet

def home(request):
    return HttpResponse('<p> home view </>')

def pet_detail(request, pet_id):
    return HttpResponse(f'<p> pet detail view with id{pet_id} </>')