from django.contrib import admin
from usermodel.models import Roles,UserRoles,CarBrands

# Register your models here.
admin.site.register(Roles)
admin.site.register(UserRoles)
admin.site.register(CarBrands)
