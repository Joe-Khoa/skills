from django.contrib import admin

# Register your models here.
from .models import Skill
from .models import Employee
from .models import Department
from .models import EmpSkills

admin.site.register(Skill)
admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(EmpSkills)

