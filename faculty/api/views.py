from rest_framework import serializers
from faculty.models import Faculty
from faculty.api.serilaizers import FacultySerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework.exceptions import AuthenticationFailed


class FacultyView(APIView):
    def get(self, request, id=None):
        try:
            if id is not None:
                faculty = Faculty.objects.get(pk=id)
                serializer = FacultySerializer(faculty)
                return Response(serializer.data, status=status.HTTP_200_OK)

            faculty = Faculty.objects.all()
            serializer = FacultySerializer(faculty, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as E:
            return Response(str(E), status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        try:
            serializer = FacultySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()

                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as E:
            return Response(str(E), status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id=None):
        try:
            if id is not None:
                faculty = Faculty.objects.get(pk=id)
                serializer = FacultySerializer(faculty, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(
                    {"error": "Please provide a valid student ID."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        except Exception as E:
            return Response(str(E), status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None):
        try:
            if id is not None:
                faculty = Faculty.objects.get(pk=id)
                serializer = FacultySerializer(faculty, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response({"msg": "Partial Data Updated"})
                return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as E:
            return Response(str(E), status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None, *args, **kwargs):
        try:
            if id is not None:
                faculty = Faculty.objects.get(pk=id)
                faculty.delete()
                return Response(status=status.HTTP_200_OK)

            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception as E:
            return Response(str(E), status=status.HTTP_400_BAD_REQUEST)
