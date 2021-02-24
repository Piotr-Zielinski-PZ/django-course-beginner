# this is where URLs for our API are gonna be stored
from django.urls import path
from profiles_api import views

urlpatterns = [
    path('hello-view/',views.HelloApiView.as_view()),
]
