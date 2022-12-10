from django.shortcuts import render
from login.models import chatUsers
from django.http import HttpResponseRedirect
import rsa
import uuid
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
        try:
            name = request.POST.get("name")
            Email = request.POST.get("Email")
            password = request.POST.get("Password")
            (pubKey, privKey) = rsa.newkeys(1024)
            pub_path = "static/keys/public_"+str(uuid.uuid4())+".pem"
            priv_path = "static/keys/private_"+str(uuid.uuid4())+".pem"
            with open(pub_path, "wb") as f:
                f.write(pubKey.save_pkcs1("PEM"))
            with open(priv_path, "wb") as f:
                f.write(privKey.save_pkcs1("PEM"))

            chatUsers.objects.create(
                name=name, email=Email, password=password, privKey=priv_path, pubKey=pub_path)
            return HttpResponseRedirect("/chat/"+str(chatUsers.objects.filter(email=Email)[0].id))
        except chatUsers.DoesNotExist:
            return render(request, "Login/signup.html")

    return render(request, "Login/signup.html")
