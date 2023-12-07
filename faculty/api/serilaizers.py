from faculty.models import Faculty
from rest_framework import serializers
from django.contrib.auth.models import User


class User(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'first_name']
        
        
class FacultySerializer(serializers.HyperlinkedModelSerializer):
    faculty = User()
    class Meta:
        model = Faculty
        fields = ['id','faculty']