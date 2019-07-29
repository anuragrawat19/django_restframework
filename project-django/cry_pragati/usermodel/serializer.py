'''writing a serializer for the models so that 
state of model objects can be converted into a 
native python datatypes that can be easily rendered into JSON,XML'''

from rest_framework import serializers
from .models  import CarBrands

#creating a serializer for Roles Model

class CarBrandsSerializer(serializers.ModelSerializer):
    class Meta:
        model=CarBrands
        fields='__all__'
