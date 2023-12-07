from django.shortcuts import render,redirect
from .models import Student
from faculty.models import Faculty
from django.contrib.auth import authenticate, login ,logout
from django. contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse 

from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url="/login/")
def home(request):
    if request.method == "POST":
        userid = request.user.id
        user_email = request.user.email
        print(userid)
        name = request.POST.get("name")
        age = request.POST.get("age")
        mobile = request.POST.get("mobile")
        image = request.FILES.get("image")
        
        
        faculty = Faculty.objects.get(faculty = userid)
        print(faculty)

        stu  = Student.objects.create(faculty=faculty,name = name,age = age, mobile=mobile, image=image)
        stu.save()
        return redirect("/")
    else:
        stu = Student.objects.all()
    
        return render(request,"home.html",{"stu":stu}) 
    return render(request,"home.html")


  
    
def update(request,id):
    stu = Student.objects.get(pk=id)
    return render (request,"update.html",{"stu":stu})

    
def doupdate(request,id):
    if request.method == "POST":
        
        name = request.POST.get("name")
        age = request.POST.get("age")
        mobile = request.POST.get("mobile")
        image = request.FILES.get("image")
        print(name,age,mobile)
    stu = Student.objects.get(pk=id)
    print(stu)
    if image:
        stu.image = image
        stu.save()
        return redirect("/")        
    stu.name = name
    stu.age = age
    stu.mobile = mobile
    stu.save()
        
    return redirect("/")
    
def delete(request,id):
    stu = Student.objects.get(pk=id)

    stu.delete()
    
        
    return redirect("/")
   
def login_page(request):
    return render(request, "login.html")

   
def register_page(request):
    return render(request, "register.html")


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
        
        return redirect("/login/")
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
            return redirect("/")
            
    return render(request,"login.html")

    
def logout_view(request):
    logout(request)
    return redirect("/login/")
        