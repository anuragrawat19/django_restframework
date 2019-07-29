from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

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

 #car brands  model
class CarBrands(models.Model):
    brandname=models.CharField(max_length=50,null=True,blank=True)
    headquarters=models.CharField(max_length=100)
    coustomer_no=models.BigIntegerField()


    class Meta:
        db_table="CarBrand"
        verbose_name_plural="Car's Brand"

    def __str__(self):
        return "%s "%self.brandname

     