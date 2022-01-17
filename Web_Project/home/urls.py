from django.urls import path
from home import views

urlpatterns = [
    #path("", views.index),
    # path (URL, views.function name, name = URL name)
    #path("", views.home, name="home"),
    path("", views.index, name="index"),
    path("sinhvien/", views.sinhvien, name="sinhvien"),
    path("monhoc/", views.monhoc, name="monhoc"),
    path("bangdiem/", views.bangdiem, name="bangdiem"),
    path("content/", views.index1, name="content"),
]
