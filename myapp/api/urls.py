# basic URL Configurations
from django.urls import include, path
from django.conf import settings
from myapp.api.views import StudentView

urlpatterns = [
    path('student/', StudentView.as_view(), name='student-list'),
    path('student/<int:pk>/', StudentView.as_view(), name='student-detail'),
    

]
