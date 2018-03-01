from django.contrib import admin

from .models import CustomModelAdmin
from .models import Department
from .models import EmpSkills
from .models import Employee
from .models import Skill


# Register your models here.
admin.site.register(Skill,CustomModelAdmin)
admin.site.register(Employee,CustomModelAdmin)
admin.site.register(EmpSkills,CustomModelAdmin)
admin.site.register(Department, CustomModelAdmin)

