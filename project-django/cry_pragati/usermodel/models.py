from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

 #creating a Snipet model
class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100,blank=True,default='')
    code=models.TextField()
    linenos=models.BooleanField(default=False)
    language=models.CharField(choices=LANGUAGE_CHOICES,default="python",max_length=100)
    style=models.CharField(choices=STYLE_CHOICES,default="friendly",max_length=100)

    def _str__(self):
        return self.language

    class Meta:
        ordering=['created']
# Create your models here.
class Roles(models.Model):
    name=models.CharField(unique=True,max_length=100,error_messages={"message":"This role already exists "})
    code=models.CharField(max_length=8,null=True,blank=True)

    class Meta:
        db_table="roles"
        verbose_name_plural="Roles"


    def __str__(self):
        return "%s " % self.name
    
    

class UserRoles(models.Model):
    user=models.OneToOneField(User)
    role=models.OneToOneField(Roles)

    class Meta:
        db_table="userrole"
        verbose_name_plural="UserRoles"

    def __str__(self):
        return "%s "%self.user

#--------------------------------------------------------------------------------

class Employees(models.Model):
    employee_name=models.CharField(max_length=50,blank=False,null=False)
    contact=models.BigIntegerField()
    salary=models.BigIntegerField()

    class Meta:
        db_table="employee"
        verbose_name_plural="Employees"


    def __str__(self):
        return "%s " % self.employee_name
    
    

class EmployeeDesignations(models.Model):
    designation=models.OneToOneField(Employees,on_delete=models.CASCADE,primary_key=True,related_name='designations')
    designation_name=models.CharField(max_length=50)

    class Meta:
        db_table="employeedesignation"
        verbose_name_plural="EmployeeDesinations"

    def __str__(self):
        return "%s "%self.designation_name
#-------------------------------------------------------------

 #car brands  model
class CarBrands(models.Model):
    brandname=models.CharField(max_length=50,null=True,blank=True,unique=True)
    headquarters=models.CharField(max_length=100)
    coustomer_no=models.BigIntegerField()


    class Meta:
        db_table="carbrand"
        verbose_name_plural="Car's Brand"

    def __str__(self):
        return "%s "%self.brandname
#---------------------------------------------------------------

#models having many-to-many field

class Students(models.Model):
    name=models.CharField(max_length=50)
    standard=models.CharField(max_length=50)
    sport=models.ManyToManyField("Sports")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural="Students"

class Sports(models.Model):
    sport_name=models.CharField(max_length=50)

    class Meta:
        verbose_name_plural="Sports"

    def __str__(self):
        return self.sport_name
    
    


     