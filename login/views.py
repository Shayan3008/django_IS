from django.shortcuts import render
from login.models import chatUsers
from django.http import HttpResponseRedirect
import os

# Create your views here.


def index(request):
    if request.method == "POST":
        try:
            Email = request.POST.get("Email")
            password = request.POST.get("Password")
            print(type(password))
            print(chatUsers.objects.filter(
                email=Email)[0].password == password)
            if chatUsers.objects.filter(email=Email)[0].password == password:
                request.session["user"] = Email
                return HttpResponseRedirect("/chat/"+str(chatUsers.objects.filter(email=Email)[0].id))
        except chatUsers.DoesNotExist:
            return render(request, "Login/login.html")

    return render(request, "Login/login.html")
