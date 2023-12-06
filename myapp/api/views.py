
from rest_framework.response import Response 
from myapp.api.serializers import StudentSerializers
from myapp.models import Student
from rest_framework.decorators import APIView
from django.shortcuts import render
from rest_framework import status
# create a viewset

class StudentView(APIView):
    def get(self, request):  # Add 'pk=None' to the get method
        try:
            student = Student.objects.all()
            serializer = StudentSerializers(student, many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as E:
            return Response(str(E),status = status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        try:
            
            serializer = StudentSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as E:
            return Response(str(E),status = status.HTTP_400_BAD_REQUEST)
            
    def put(self, request,pk=None):  # Add 'pk=None' to the put method
        try:
            if pk is not None:
           
                book = Student.objects.get(pk=pk)
                serializer = StudentSerializers(book, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Please provide a valid book ID.'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as E:
            return Response(str(E),status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):  # Add 'pk=None' to the delete method
        try:

            if pk is not None:
                book = Student.objects.get(pk=pk)
                book.delete()
                return Response(status=status.HTTP_200_OK)
            else:
            
                return Response(status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as E:
            return Response(str(E),status = status.HTTP_400_BAD_REQUEST)
        
        