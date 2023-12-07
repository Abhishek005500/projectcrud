from django.urls import path
# from .views import *
from myapp import views

urlpatterns = [
    
    path('', views.home,name="home"),

    path('update/<int:id>', views.update,name="update"),
    path('doupdate/<int:id>', views.doupdate,name="doupdate"),
    
    path('delete/<int:id>', views.delete,name="delete"),
    
   
    
]
