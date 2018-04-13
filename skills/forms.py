from django.forms import ModelForm
from .models import EmpSkills

class EmppSkillsForm(ModelForm):
     class Meta:
       model=EmpSkills  
       exclude=['id']
     
     def __init__(self, *args, **kwargs):
       self.request = kwargs.pop('request', None)
        # print(self.request.user)
       super(EmppSkillsForm, self).__init__(*args, **kwargs)
   