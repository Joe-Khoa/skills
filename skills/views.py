from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
from .models import EmpSkills,Employee
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import employeesSerializers 
from .forms import EmppSkillsForm
import requests





# Create your views here.
@login_required
def my_view(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=2ac3ec34f1ed7bfc53718ba5b3ae3800'
    cities =['London','New York']
    weather_data = []

    for city in cities:

        r = requests.get(url.format(city)).json()
       
        city_weather = {
            'city' : city,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
        }

        weather_data.append(city_weather)

    context = {'weather_data' : weather_data}
    
    
    
    
    return render(request,'home.html', context)

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
    
from django.http import HttpResponseRedirect    
from crudbuilder.views import ViewBuilder
from crudbuilder.helpers import reverse
from skills.crud import EmpSkillsCrud

builder = ViewBuilder('skills', 'empSkills', EmpSkillsCrud)
builder.generate_crud()

EmpSkillsListView = builder.classes['EmpSkillsListView']
EmpSkillsCreateView = builder.classes['EmpSkillsCreateView']
EmpSkillsUpdateView = builder.classes['EmpSkillsUpdateView']
EmpSkillsDetailView = builder.classes['EmpSkillsDetailView']


class MyCustomEmpSkillsListView(EmpSkillsListView):
    def get_context_data(self, **kwargs):
        context = super(MyCustomEmpSkillsListView, self).get_context_data(**kwargs)
        context['your_template_variable'] = 'Your new template variable'
        return context

    def get_queryset(self):
        # return super(MyCustomPersonListView, self).get_queryset()
        return self.model.objects.none()


class MyCustomEmpSkillsDetailView(EmpSkillsDetailView):
    def get_context_data(self, **kwargs):
        context = super(MyCustomEmpSkillsDetailView, self).get_context_data(**kwargs)
        # context['form'] = YourAnotherForm
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = EmppSkillsForm(request.POST)
        if form.is_valid():
            # Do your custom logic here
            pass
        return HttpResponseRedirect(
            reverse(
                'person-detail',
                args=[self.object.employee]
            )
        )


class MyCustomEmpSkillsCreateView(EmpSkillsCreateView):
    def form_valid(self, form):
        instance = form.save(commit=False)
        # instance.created_by = self.request.user
        instance.save()
        # # your custom logic goes here
        return HttpResponseRedirect(reverse('mycustom-people'))    
    

