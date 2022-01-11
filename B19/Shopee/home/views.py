from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'home/index.html')
    # return HttpResponse("Hello, Django!")


"""
# Replace the existing home function with the one below
def home(request):
    return render(request, "hello/home.html")

def about(request):
    return render(request, "hello/about.html")

def contact(request):
    return render(request, "hello/contact.html")

"""
