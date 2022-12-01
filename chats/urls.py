from django.contrib import admin
from django.urls import path
from chats import views
urlpatterns = [
    path("<userId>/", view = views.index, name="Chats"),
    # For audio HTTP REQUEST HANDLING
    path("audio/aud/", view = views.audio, name="Audio Saving"),
    # For Getting ALL CHATS Of a room
    path("chats/<groupId>/", view=views.chats, name="Get All Chats")
]
