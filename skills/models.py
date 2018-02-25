from django.db import models
from django.contrib import admin
# Create your models here.

        
class Department(models.Model):
   
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)
    def __str__(self):
         return  self.name
    class Meta:
        managed = True
        db_table = 'department'
        
   
        
class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)
    def __str__(self):
         return  self.name
    department = models.ForeignKey(Department, models.DO_NOTHING, blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'employee'  
       
            
        
          
        
class EmpSkills(models.Model):
    id = models.AutoField(primary_key=True)
    year = models.IntegerField(blank=True, null=True)
    quarter = models.IntegerField(blank=True, null=True)
    employee = models.ForeignKey('Employee', models.DO_NOTHING, blank=True, null=True)
    skill = models.ForeignKey('Skill', models.DO_NOTHING, blank=True, null=True)
    grade = models.IntegerField()
    


    class Meta:
        managed = False
        db_table = 'emp_skills'
        unique_together = (('year', 'quarter', 'employee', 'skill'),)





class Skill(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'skill'
        
    def __str__(self):
         return  self.name   
        
        
        
        
MySpecialAdmin = lambda model: type('SubClass'+model.__name__, (admin.ModelAdmin,), {
    'list_display': [x.name for x in model._meta.fields ] ,
    'list_select_related': [x.name for x in model._meta.fields if isinstance(x, (models.ManyToOneRel, models.ForeignKey, models.OneToOneField,))]
})        
        
        



