from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
from .models import EmpSkills,Employee
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import employeesSerializers 





# Create your views here.
@login_required
def my_view(request):
    return render(request,'home.html', context=None)

@login_required
def emp_skills(request):
   
    emp_skills_list = EmpSkills.objects.all()
    paginator = Paginator(emp_skills_list, 3) # Show 25 contacts per page

    page = request.GET.get('page')
    emp_skills_list = paginator.get_page(page)
    return render(request, 'skills/emp_skills_list.html', {'list': emp_skills_list})

class employeeList(APIView):
    
    def get(self,request):
        employees=Employee.objects.all()
        serializer=employeesSerializers(employees,many=True)
        return Response(serializer.data)
        
    def post(self):  
        pass  
    

