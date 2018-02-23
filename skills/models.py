from django.db import models

# Create your models here.

        
class Department(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'department'
        
class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=10)
    department = models.ForeignKey(Department, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee'        
        
class EmpSkills(models.Model):
    id = models.IntegerField(primary_key=True)
    year = models.IntegerField(blank=True, null=True)
    quarter = models.IntegerField(blank=True, null=True)
    employee = models.ForeignKey('Employee', models.DO_NOTHING)
    skill = models.ForeignKey('Skill', models.DO_NOTHING, blank=True, null=True)
    grade = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'emp_skills'
        unique_together = (('year', 'quarter', 'employee', 'skill'),)





class Skill(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'skill'



