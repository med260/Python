from django.shortcuts import render


tasks = ["foo " , "bar " , "baz"]

# Create your views here.
def index(request) : 
    return render(request , "tasks/index.html" ,{
        "tasks" : tasks
    })

def add(request):
    # newtask = str(input("Add New Task :" ))
    # tasks.append(newtask)
    return render(request , "tasks/add.html" , {

    })