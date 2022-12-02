from django.shortcuts import render
from login.models import chatUsers
from django.http import HttpResponseRedirect
# Create your views here.


def index(request):
    if request.method == "POST":
        try:
            Email = request.POST.get("Email")
            password = request.POST.get("Password")
            user = chatUsers.objects.filter(email=Email)
            if user.exists:
                if user[0].password == password:
                    request.session["user"] = Email
                    return HttpResponseRedirect("/chat/"+str(user[0].id))
        except chatUsers.DoesNotExist:
            return render(request, "Login/login.html")

    return render(request, "Login/login.html")


def signup(request):
    if request.method == "POST":
        print("Hello World")
        try:
            name = request.POST.get("name")
            Email = request.POST.get("Email")
            password = request.POST.get("Password")
            id1 = chatUsers.objects.create(
                name=name, email=Email, password=password).id
            return HttpResponseRedirect("/chat/"+str(chatUsers.objects.filter(email=Email)[0].id))
        except chatUsers.DoesNotExist:
            return render(request, "Login/signup.html")

    return render(request, "Login/signup.html")
