from django.shortcuts import render
from login.models import chatUsers
# Create your views here.
def index(request):
    
    if request.method == "POST":
        try:
            Email = request.POST.get("Email")
            password = request.POST.get("password")
            print(chatUsers.objects.filter(email = Email)[0].id)
        except chatUsers.DoesNotExist:
            return render(request,"Login/login.html")

    return render(request,"Login/login.html")