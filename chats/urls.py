from django.contrib import admin
from django.urls import path
from chats import views
urlpatterns = [
    path("<userId>/",views.index,name="Chats"),
    path("audio/aud/",views.audio,name="Audio Saving")#For audio HTTP REQUEST HANDLING
]