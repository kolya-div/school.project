from django.shortcuts import render
from .models import StudentModel
from .serializers import StudentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.status import HTTP_201_CREATED


class StudentAllView(APIView):
    def get(self, request,*args,**kwargs):
        students = StudentModel.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    
class StudentDetailView(APIView):
    def get(self, request,*args,**kwargs):
        student_id = kwargs['id']
        student_data = get_object_or_404(StudentModel,id=student_id)
        serializer = StudentSerializer(student_data)
        return Response(serializer.data)
    
class StudentCreateView(APIView):
    def post(self, request,*args,**kwargs):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": "baza qosili"}, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=400)
    
class StudentUpdateView(APIView):
    def put(self, request,*args,**kwargs):
        student_id = kwargs['id']
        student_data = get_object_or_404(StudentModel,id=student_id)
        serializer = StudentSerializer(instance=student_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": "baza janaladniiii"}, status=200)
        return Response(serializer.errors, status=400)
    
class StudentDeleteView(APIView):
    def delete(self, request,*args,**kwargs):
        student_id = kwargs['id']
        student_data = get_object_or_404(StudentModel,id=student_id)
        student_data.delete()
        return Response({"data": "baza ochirildi"}, status=200)


# Create your views here.
