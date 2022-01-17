from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.


def index(request):
    # return HttpResponse("Hello world!")
    return render(request, 'home/index.html')


def sinhvien(request):
    return render(request, 'home/sinhvien.html')


def monhoc(request):
    return render(request, 'home/monhoc.html')


def bangdiem(request):
    return render(request, 'home/bangdiem.html')

######################################################


def index1(request):
    return render(request, 'home/content.html')
