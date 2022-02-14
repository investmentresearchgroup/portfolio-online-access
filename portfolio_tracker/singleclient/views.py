from django.shortcuts import render

# Create your views here.
def index(request):
    context = {"greet":"Hello!"}
    return render(request,"singleclient/index.html",context=context)
