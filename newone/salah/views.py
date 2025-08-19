from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request , "hello/index.html")
 
def salah(request) : 
    return HttpResponse ("this is response of the new function ")

def greet(request , name) : 
    return render (request , "hello/greet.html" , {
        "name" : name.capitalize()
         
    })

 