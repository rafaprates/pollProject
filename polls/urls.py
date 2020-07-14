from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'), #displays views.index at polls/
    path('foo', views.index, name="bar") # displays views.index at polls/foo
]