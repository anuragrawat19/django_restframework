from django.shortcuts import render,get_object_or_404
from rest_framework import status
from django.http import HttpResponse,JsonResponse
from .models import CarBrands,Employees,EmployeeDesignations,Snippet # importing the models 
from rest_framework.views import APIView#importing a APIView class based views from rest_framwork 
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer #for serializing the objects into json form
from rest_framework.parsers import JSONParser
from .serializer import * # importing the serializer for each models
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
        car=CarBrands.objects.filter(brandname__icontains=alpha_bet)
        if len(car)==0:
            return Response({"sdsdf":"No such car brand is available"})
        else:
            serializer_class=CarBrandsSerializer(car,many=True)
            return  Response(serializer_class.data)
    

class Employeeslist(APIView):
    def get(self,request):
        Employee=Employees.objects.all()
        serialize_class=EmployeeNameSerializer(Employee,many=True)
        return Response(serialize_class.data)

class Employeesdetails(APIView): #view for the employees details and  for adding a new employee
    def get (self,request):
        Employee=Employees.objects.all()
        serialize_class=EmpDetailSerializer(Employee,many=True)
        return Response(serialize_class.data)
    
    def post(self,request):
        serializer_class=EmpDetailSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response("New employee {} is added".format(serializer_class.data["employee_name"]))
        else:
            return Response({"status":0,"error-message":"data is not valid"})

class DesignationList(APIView): #view for the list of all the designation and  for adding a new employee designation
    def get(self,request):
        desination=EmployeeDesignations.objects.values("designation_name").distinct()
        serialize_class=EmployeeDesignationsSerializer(desination,many=True)
        return Response({"list of all the designations that this company has":serialize_class.data})
    
    def post(self,request):
        serializer_class=EmployeeDesignationsSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response("New designation {} is added".format(serializer_class.data["designation"]))

        # designation_id=request.data.get("designation")
        # designation=request.data.get("designation_name")
        # new_designation=EmployeeDesignations.objects.create(designation_id=designation_id,designation=designation)

      



