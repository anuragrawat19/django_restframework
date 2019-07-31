from django.contrib import admin
from usermodel.models import Roles,UserRoles,CarBrands,Employees,EmployeeDesignations,Students,Sports,Snippet

# Register your models here.
admin.site.register(Roles)
admin.site.register(UserRoles)
admin.site.register(CarBrands)
admin.site.register(Employees)
admin.site.register(EmployeeDesignations)
admin.site.register(Students)
admin.site.register(Sports)
admin.site.register(Snippet)
