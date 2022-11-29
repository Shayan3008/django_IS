from django.shortcuts import render, HttpResponse
from chats.audio.audioEncryption import audioEncrypt
from login.models import chatUsers
from django.http import HttpResponseRedirect
from chats.audio.keyGeneration import keyGeneration

# Create your views here.


def index(request, userId):
    print(request.session)
    if request.session.has_key("user") == False :
        return HttpResponseRedirect("/")
    context = {}
    context["User"] = chatUsers.objects.exclude(id=int(userId))
    context["Id"] = userId
    # return HttpResponse("This is Response")
    return render(request, "chats/chat.html", context)


def audio(request):
    if request.method == "POST":
        if request.FILES.get("myAudio", False):
            handleUploadFile(request.FILES["myAudio"])
            Key = keyGeneration()
            return HttpResponse(audioEncrypt(Key))
        return HttpResponse("NO FILE FOUND")


def handleUploadFile(f):
    with open("chats/audio/" + f.name, "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)
