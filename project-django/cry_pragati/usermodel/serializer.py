'''writing a serializer for the models so that 
state of model objects can be converted into a 
native python datatypes that can be easily rendered into JSON,XML'''

from rest_framework import serializers
from .models  import CarBrands,EmployeeDesignations,Employees,Snippet,LANGUAGE_CHOICES,STYLE_CHOICES

#creating a serializer for Snippet model

class SnippetSerializerA(serializers.Serializer):# SnippetSerializer using 'serializers'
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField( max_length=100)
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
        instance.code = validate_data.get('code', instance.code)
        instance.linenos = validate_data.get('linenos', instance.linenos)
        instance.language = validate_data.get('language', instance.language)
        instance.style = validate_data.get('style', instance.style)
        instance.save()
        return instance


class SnippetSerializerB(serializers.ModelSerializer):# SnippetSerializer using 'ModelSerializer'
    class Meta:
        model = Snippet
        fields="__all__"




#creating a serializer for Roles Model

class CarBrandsSerializer(serializers.ModelSerializer):
    class Meta:
        model=CarBrands
        fields='__all__'

#creating serializer for list of all the names of employee in  Employees Model
class EmployeeNameSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employees
        fields=["employee_name"]


#creating a serialzer for getting  details of all the employees
class EmpDetailSerializer(serializers.ModelSerializer):
    def length(value):
        if len(value)!=10:
            raise serializers.ValidationError(" contact should contain 10 digits only")

    designations=serializers.SlugRelatedField(slug_field="designation_name",read_only=True)
    employee_name=serializers.CharField(max_length=50)
    contact=serializers.CharField(validators=[length])
    

    def validate_employee_name(self,value): #validation  for employee_name field that it should contain mr or mrs
        a="mr"
        if a not in value.lower() : 
            raise serializers.ValidationError('this employee name  should contain Mr or Mrs')
        return value
    class Meta:
        model=Employees
        fields="__all__"


#creatimg a serializer for model employees
class EmpSerializer(serializers.Serializer):
    employee_name=serializers.CharField(max_length="50")
    contact=serializers.IntegerField()
    salary=serializers.CharField(max_length=20)



class EmployeeDesignationsSerializer(serializers.Serializer):
    designation=EmpSerializer()
    designation_name = serializers.CharField(required=True, allow_blank=False, max_length=100)
    def create(self,validate_data):

        '''create and return a new Snippet'''
        return EmployeeDesignations.objects.create(**validate_data)
    

    def update(self,instance,validate_data):
        ''' Update and return an existing snippet'''
        instance.designation_name = validated_data.get('designaion_name', instance.designation_name)
        instance.save()
        return instance


