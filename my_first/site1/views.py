from django.shortcuts import render
from django.http import HttpResponse
from . import models, form

def index(request):
    return render(request,"base.html")
def about(request):
    if request.method == "POST":
        name = request.POST.get("name")
        date = request.POST.get("date")
        print(name, date)
        form1 = form.Form1(request.POST)
        if form1.is_valid():
            return HttpResponse("<h1>Форма валидна</h1>")

    else:
        form1 = form.Form1()

    context = {
        "zap": "text1",
        "zap1":models.Model1.objects.all(),
        "form":form1,
    }
    return render(request,"about.html",context)
def contacts(request):
    return render(request,"contacts.html")
def user1(request,user):
    return HttpResponse(f"<h2>Имя {user}</h2>")
def user(request,user,age):
    return HttpResponse(f"<h2>Имя {user}, Возраст {age}</h2>")
