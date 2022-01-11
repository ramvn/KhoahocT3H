from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index1(request):
    return HttpResponse("This is kinhte")


def index2(request):
    return HttpResponse("This is Sport")


def index3(request):
    return HttpResponse("This is Thitruong")
