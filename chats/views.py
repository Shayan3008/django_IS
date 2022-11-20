from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    context = {
        "variable":"This is sent"
    }
    # return HttpResponse("This is Response")
    return render(request,"index.html",context)