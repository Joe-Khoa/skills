from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import EmpSkills





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
    
    

