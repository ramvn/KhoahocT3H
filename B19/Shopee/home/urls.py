from django.urls import path
#from home import views
from . import views

urlpatterns = [
    path("", views.index),
    # Application folder urls.py
    # path (URL, views.function name, name = URL name)
    #path("", views.index, name="index"),
    # path ("test/"", views.test, name ="test"),
]
