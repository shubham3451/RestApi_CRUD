from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.response import Response
from .models import data
from .serializers import dataserializers
from rest_framework import status

# Create your views here.
class data_api(APIView):
    def get(self,request, pk=None, format=None):
        id = pk
        if id is not None:
            stu = data.objects.get(id=id)
            serializer = dataserializers(stu)
            return Response(serializer.data)
        stu = data.objects.all()
        serializer = dataserializers(stu,many=True)
        return Response(serializer.data)
    
    def post(self,request, pk=None,format=None):
        serializer = dataserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': "data created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk=None, format=None):
        id = pk
        stu = data.objects.get(pk=id)
        serializer = dataserializers(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'data updated'},status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,pk=None,format=None):
        id = pk
        stu = data.objects.get(pk=id)
        serializer = dataserializers(stu, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'data updated'},status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk=None,format=None):
        id = pk
        stu = data.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'data deleted'})
