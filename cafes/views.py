from django.shortcuts import render
from django.http import HttpResponse


def cafes(request):
    context = {}
    return HttpResponse("Hello World! You are at the everywhere cafe landing page")

    # Create your views here.
