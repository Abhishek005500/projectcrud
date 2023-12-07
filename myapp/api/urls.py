# basic URL Configurations
from django.urls import include, path
from django.conf import settings
from myapp.api.views import StudentView

urlpatterns = [
    path('show/', StudentView.as_view(), name='student-list'),
    path('show/<int:pk>/', StudentView.as_view(), name='student-detail'),
    

]
