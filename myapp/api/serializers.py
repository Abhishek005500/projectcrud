from rest_framework import serializers
from myapp.models import Student,User

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model  = Student
        fields = ('id','name','age','mobile','image','faculty')
        
       
        
        