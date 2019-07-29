from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import CarBrands # importing the models 
from rest_framework.views import APIView#importing a APIView class based views from rest_framwork 
from rest_framework.response import Response
from .serializer import CarBrandsSerializer # importing the serializer for teh models taht we created 

# Create your views here.
#creating a view for rendering a data of  the Car Brands Model

class CarBrand(APIView):
    def get(self,request):
        CarBrand=CarBrands.objects.all()
        serialize_class=CarBrandsSerializer(CarBrand,many=True)
        return Response({"CarBrands":serialize_class.data})
    
    def post(self,request):
        serializer=CarBrandsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":2,"message":"Sucessfully created"})
        else:
            return Response({"status":0,"error-message":"errors"})
    
    def put(request,brand_id):
        brand=get_object_or_404(CarBrands.objects.all(),pk=brand_id)
        serializer=CarBrandsSerializer(instance=brand,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":2,"message":"Sucessfully modified"})
        else:
            return Response({"staus":0,"error-message":"data is not modified "})

    def delete(self, request, brand_id):
    # Get object with this pk
        brand = get_object_or_404(Article.objects.all(), pk=brand_id)
        brand.delete()
        return Response({"message": "Article with id `{}` has been deleted.".format(pk)},status=204)

