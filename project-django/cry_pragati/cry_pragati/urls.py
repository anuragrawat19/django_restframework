"""cry_pragati URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from usermodel import views


urlpatterns = [
    # for list of all the car brand and adding a new brand
    url(r'^admin/', admin.site.urls),
    # view a particular car brand
    url(r'^carbrandlist/$', views.CarBrand.as_view()),
    url(r'^carbrandlist/(?P<pk>[0-9]+)/$', views.CarBrandDetails.as_view()),
    url(r'^carbrandlist/search/(?P<alpha_bet>\w+)/$', views.FetchCar.as_view()),
    url(r'^employees_list/$', views.Employeeslist.as_view()),
    url(r'^employees_details/$', views.Employeesdetails.as_view()),
    url(r'^designations_list/$', views.DesignationList.as_view()),
    url(r'^snippet_list/$', views.Snippet_list.as_view()),
    url(r'^snippet_list/(?P<pk>[0-9]+)/$', views.Snippet_list.as_view()),
    url(r'^person_tasks/$', views.UserTasklist.as_view()),

]
