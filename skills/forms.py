from django.forms import ModelForm
from .models import EmpSkills

class EmppSkillsForm(ModelForm):
     class Meta:
       model=EmpSkills  
       exclude=['id']
        