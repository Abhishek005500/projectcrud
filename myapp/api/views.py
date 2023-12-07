
from rest_framework.response import Response 
from myapp.api.serializers import StudentSerializers
from myapp.models import Student,User
from rest_framework.decorators import APIView
from django.shortcuts import render
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed

# create a viewset

class StudentView(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(pk=id)
            serializer = StudentSerializers(stu)
            return Response(serializer.data)
        
        stu = Student.objects.all()
        serializer = StudentSerializers(stu, many=True)
        return Response(serializer.data)  

    def post(self, request, *args, **kwargs):
        try:
            
            serializer = StudentSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as E:
            return Response(str(E),status = status.HTTP_400_BAD_REQUEST)
            
    def put(self, request,pk=None): 
        try:
            id = pk
            if pk is not None:
            
                student = Student.objects.get(pk=id)
                serializer = StudentSerializers(student, data=request.data)
                if serializer.is_valid():
                    serializer.save() 
                    return Response(serializer.data, status=status.HTTP_200_OK)
                return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
            else:
                return Response({'error': 'Please provide a valid student ID.'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as E:
            return Response(str(E),status = status.HTTP_400_BAD_REQUEST)
        
    
    def patch(self, request, pk = None, format=None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializers(stu, data= request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Updated'})
        return Response(serializer.errors)    

    def delete(self, request,pk = None, *args, **kwargs):  # Add 'pk=None' to the delete method
        try:
            
            id = pk
            if pk is not None:
                
                student = Student.objects.get(pk=id)
                student.delete()
                return Response(status=status.HTTP_200_OK)
            else:
            
                return Response(status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as E:
            return Response(str(E),status = status.HTTP_400_BAD_REQUEST)
        

        
              