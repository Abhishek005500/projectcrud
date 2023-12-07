from django.urls import path
from django.conf import settings
from faculty.api.views import FacultyView
urlpatterns = [
    
    path('faculty/',FacultyView.as_view()),
    path('faculty/<int:id>/',FacultyView.as_view()),

]
