from django.shortcuts import render,get_object_or_404
from rest_framework import status
from django.http import HttpResponse,JsonResponse
from .models import CarBrands,Employees,EmployeeDesignations,Snippet # importing the models 
from rest_framework.views import APIView#importing a APIView class based views from rest_framwork 
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer #for serializing the objects into json form
from rest_framework.parsers import JSONParser
from .serializer import CarBrandsSerializer,EmployeeSerializer, EmployeeDesignationsSerializer,SnippetSerializerA,SnippetSerializerB # importing the serializer for each models
from rest_framework.decorators import api_view

# Create your views here.
#creating a view for the Snippet model
class Snippet_list(APIView):
    '''List all snippets,or create a new snippet'''
    def get(self,request):
        snipets=Snippet.objects.all()
        seriliazer_class=SnippetSerializerA(snipets,many=True)
        return Response({"Snippet_details":seriliazer_class.data})
    
    def post(self,request):#for adding a snippet
        seriliazer_class=SnippetSerializerB(data=request.data)
        if seriliazer_class.is_valid():
            seriliazer_class.save()
            return Response({"status":"snippet sucessfully created"},status=201)
        else:
            return Response({"status":"snippet creation failed"},status=401)
        


#creating a view for rendering a data of  the Car Brands Model

class CarBrand(APIView):
    def get(self,request): #for getting a list of all the car models
        CarBrand=CarBrands.objects.all()
        serialize_class=CarBrandsSerializer(CarBrand,many=True)
        return Response({"CarBrands":serialize_class.data})

    
    def post(self,request): # for adding a new car brand
        serializer=CarBrandsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":2,"message":"Sucessfully created"})
        else:
            return Response({"status":0,"error-message":"errors"})


class CarBrandDetails(APIView):

    def get(self, request, pk):
        state = CarBrands.objects.get(pk=pk)
        serializer = CarBrandsSerializer(state)
        return Response(serializer.data)

    

class FetchCar(APIView):
    def get(self,request,alpha_bet):
        try:
            car=CarBrands.objects.filter(brandname__icontains=alpha_bet)
        except CarBrands.DoesNotExist:
            return Response({"sdsdf":"No such car brand is available"})
        serializer_class=CarBrandsSerializer(car,many=True)
        return  Response(serializer_class.data)
    


# @api_view(['GET','PUT'])
# def brand_details(request,pk):
#     try:
#         brand_details=CarBrands.objects.get(pk=pk)
#     except CarBrands.DoesNotExist:
#         return Response({"status":"HTTP_404_NOT_FOUND"})
#     if request.method=='GET': #for getting a details of a particular car brand 
#         serializer_class=CarBrandsSerializer(brand_details)
#         return Response(serializer_class.data )
#     elif request.method=='PUT': # for updating  the details of an existing  car brand
#         serializer=CarBrandsSerializer(brand_details,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"carbrand id {} successfully updated. ".format(pk)},status=204)
#         else:
#             return Response({"error status: carbrand id {} did not updated".format(pk)})



class Employeesdetails(APIView):
    def get (self,request):
        Employee=Employees.objects.all()
        serialize_class=EmployeeSerializer(Employee,many=True)
        return(Response(serialize_class.data))

