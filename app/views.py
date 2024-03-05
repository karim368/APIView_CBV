from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import APIView
from rest_framework.response import Response
from app.serializers import *

class ProductModelCrud(APIView):
    def get(self,request,id):
        pdobj = Product.objects.all()
        jsonobj = ProductModelSerializer(pdobj,many=True)
        jsondata = jsonobj.data
        return Response(jsondata)
    
    def post(self,request,id):
        jsonobj = request.data
        jsondata = ProductModelSerializer(data=jsonobj)
        if jsondata.is_valid():
            jsondata.save()
            return Response({'insert':'Data is inserted successfully'})
        else:
            return Response({'error':'Data is not inserted'})
        
    def put(self,request,id):
        ormobj = Product.objects.get(id=id)
        ormdata = ProductModelSerializer(ormobj,data=request.data)
        if ormdata.is_valid():
            ormdata.save()
            return Response({'update':'Data is updated'})
        else:
            return Response({'error':'data is not updated'})

    def patch(self,request,id):
        ormobj = Product.objects.get(id=id)
        ormdata = ProductModelSerializer(ormobj,data=request.data,partial=True)
        if ormdata.is_valid():
            ormdata.save()
            return Response({'update':'Data is updated'})
        else:
            return Response({'error':'data is not updated'})
        
    def delete(self,requset,id):
        Product.objects.get(id=id).delete()
        return Response({'delete':'Data is deleted'})


    