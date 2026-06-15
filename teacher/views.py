from django.shortcuts import render
from .models import TecherModel
from .serializers import TecherSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.status import HTTP_201_CREATED


class TecherAllView(APIView):
    def get(self, request,*args,**kwargs):
        teachers = TecherModel.objects.all()
        serializer = TecherSerializer(teachers, many=True)
        return Response(serializer.data)

class TecherDetailView(APIView):
    def get(self, request,*args,**kwargs):
        teacher_id = kwargs['id']
        teacher_data = get_object_or_404(TecherModel,id=teacher_id)
        serializer = TecherSerializer(teacher_data)
        return Response(serializer.data)
    
class TecherCreateView(APIView):
    def post(self, request,*args,**kwargs):
        serializer = TecherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": "baza qosili"}, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=400)
    
class TecherUpdateView(APIView):
    def put(self, request,*args,**kwargs):
        teacher_id = kwargs['id']
        teacher_data = get_object_or_404(TecherModel,id=teacher_id)
        serializer = TecherSerializer(instance=teacher_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": "baza janaladniiii"}, status=200)
        return Response(serializer.errors, status=400)
    
class TecherDeleteView(APIView):
    def delete(self, request,*args,**kwargs):
        teacher_id = kwargs['id']
        teacher_data = get_object_or_404(TecherModel,id=teacher_id)
        teacher_data.delete()
        return Response({"data": "baza dan oshirildi"}, status=200)




# Create your views here.
