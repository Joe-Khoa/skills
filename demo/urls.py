"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from skills import views


admin.autodiscover()
admin.site.site_header = 'Skills Administration' 
admin.site.index_title = ('Skills Admin') 
admin.site.site_title = ('Skills Admin page')
admin.site.site_url='/accounts/profile/'

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include('django.contrib.auth.urls')),
    path('accounts/profile/',views.my_view, name='home'),
    path('skills/emp_skills_list/',views.emp_skills,name='emp_skills'),
    path('employees/',views.employeeList.as_view(),name='rest_emp'),
    path('crud/',include('crudbuilder.urls')),
    
]
