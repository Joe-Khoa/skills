from django.contrib import admin

# Register your models here.
from .models import Skill
from .models import Employee
from .models import Department
from .models import EmpSkills
from .models import MySpecialAdmin

admin.site.register(Skill,MySpecialAdmin(Skill))
admin.site.register(Employee,MySpecialAdmin(Employee))
admin.site.register(EmpSkills,MySpecialAdmin(EmpSkills))
admin.site.register(Department, MySpecialAdmin(Department))

