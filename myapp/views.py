from django.shortcuts import render,redirect
from .models import Student

# Create your views here.


def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        mobile = request.POST.get("mobile")
        image = request.FILES.get("image")
        
        print(image)
        stu  = Student.objects.create(name = name,age = age, mobile=mobile, image=image)
        Student.save(stu)
        
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
   