# basic URL Configurations
from django.urls import include, path
from django.conf import settings

# import routers
# from rest_framework import routers
# import everything from views
from .views import *
from myapp.api import views 
# define the router
# router = routers.DefaultRouter()
 
# define the router path and viewset to be used
# router.register(r'geeks', StudentViewSet)
 
# specify URL Path for rest_framework
from django.urls import path
from myapp.api.views import StudentView

urlpatterns = [
    path('student/', StudentView.as_view(), name='student-list'),
    path('student/<int:pk>/', StudentView.as_view(), name='student-detail'),
]
