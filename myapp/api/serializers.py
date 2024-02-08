from rest_framework import serializers
from myapp.models import Student


class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ("id", "name", "age", "mobile", "image", "faculty")
        