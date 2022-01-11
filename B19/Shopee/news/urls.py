from django.urls import path
#from home import views
from . import views

urlpatterns = [
    #path("", views.index, name="index"),
    path("kinh-te", views.index1),
    #path("kinh-te", views.index1, name="index1"),
    path("the-thao", views.index2),
    path("thi-truong", views.index3),
]
