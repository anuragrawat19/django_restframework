'''writing a serializer for the models so that 
state of model objects can be converted into a 
native python datatypes that can be easily rendered into JSON,XML'''

from rest_framework import serializers
from .models  import CarBrands,EmployeeDesignations,Employees,Snippet,LANGUAGE_CHOICES,STYLE_CHOICES

#creating a serializer for Snippet model

class SnippetSerializerA(serializers.Serializer):# SnippetSerializer using 'serializers'
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    def create(self,validate_data):
        '''create and return a new Snippet'''
        return Snippet.objects.create(**validate_data)
    

    def update(self,instance,validate_data):
        ''' Update and return an existing snippet'''
        instance.title = validate_data.get('title',instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance


class SnippetSerializerB(serializers.ModelSerializer):# SnippetSerializer using 'ModelSerializer'
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']




#creating a serializer for Roles Model

class CarBrandsSerializer(serializers.ModelSerializer):
    class Meta:
        model=CarBrands
        fields='__all__'

#creating serializer for  Employees and EmployeeDesignations
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employees
        fields='__all__'

class EmployeeDesignationsSerializer(serializers.ModelSerializer):
    Employee=EmployeeSerializer()
    class Meta:
        model=EmployeeDesignations
        fields='__all__'
