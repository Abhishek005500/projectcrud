from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method == "POST":
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username,password)
        
        
        user =  User.objects.create(first_name=firstname,last_name=lastname,username=username)
        print(user)
        user.set_password(password)
        user.save()
        
        return redirect("/fac/login/")
    return render(request,"register.html")




def login_view(request):
    if request.method =="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username,password)
        



        user = authenticate( username=username, password=password)
        
        print(user)
        if user is None:
            messages.error(request,"Invalid username or password")
            
        else:
            login(request, user)
            return redirect("/student/")
            
    return render(request,"login.html")

    
def logout_view(request):
    logout(request)
    return redirect("/fac/login/")
        