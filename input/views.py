from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "input/index.html")

def greet(request):
    
    name = request.POST['name']

    return render(request, "input/greet.html", {'name': name.capitalize()})

 