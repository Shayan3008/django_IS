from django.shortcuts import render, HttpResponse
from chats.audio.audioEncryption import audioEncrypt
from login.models import chatUsers
from django.http import HttpResponseRedirect
from chats.audio.keyGeneration import keyGeneration
from chats.models import KeyRoom
from chats.models import Chats
from kellanb_cryptography import aes
import json

# Create your views here.


def index(request, userId):
    if request.session.has_key("user") == False:
        return HttpResponseRedirect("/")
    context = {}
    context["User"] = chatUsers.objects.exclude(id=int(userId))
    context["Id"] = userId
    # return HttpResponse("This is Response")
    return render(request, "chats/chat.html", context)


def audio(request):
    if request.method == "POST":
        if request.FILES.get("myAudio", False):
            group_id = request.POST.get("id")
            handleUploadFile(request.FILES["myAudio"])
            keyObject = KeyRoom.objects.filter(groupId=group_id)
            if keyObject.exists:

                path = audioEncrypt(
                    keyObject[0].key)
            else:
                Key = keyGeneration()
                KeyRoom.objects.create(groupId=group_id, key=Key)
                path = audioEncrypt(Key)
            return HttpResponse(path)
        return HttpResponse("NO FILE FOUND")


def handleUploadFile(f):
    with open("chats/audio/" + f.name, "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def chats(request, groupId):
    chats = Chats.objects.filter(groupId=groupId)
    if chats.exists:
        data = list(chats.values())
        keyObject = KeyRoom.objects.filter(groupId=groupId)[0].key
        for i in range(len(data)):
            if data[i]['Audio'] == None:
                data[i]['EncryptedText'] = aes.decrypt_aes(
                    data[i]['EncryptedText'], keyObject)
        return HttpResponse(json.dumps(data))
