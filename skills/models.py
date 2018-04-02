from django.contrib import admin
from django.db import models
from django.db.models.fields import URLField
from django.urls import path
from django.utils.safestring import mark_safe
from numpy.random import random_sample
import pygal
from pygal.style import DarkStyle
import pandas as pd
from collections import defaultdict

import numpy


# Create your models here.
class Department(models.Model):
   
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)
    def __str__(self):
         return  self.name
  
    def get_data(self):
        """ 
        Fake Method to generate random data.
        In the real case, this method should arrange
        data to be plotted according to model instance
        fields' values.
        """
        return random_sample(5)
    class Meta:
        managed = True
        db_table = 'department'
     
  
        
class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)
    get_data=URLField()
    
    def __str__(self):
        return  self.name
     
    department = models.ForeignKey(Department, models.DO_NOTHING, blank=True, null=True)
    def empSkills(self):
        return EmpSkills.objects.filter(employee=self)
   
    def get_data(self):
         
        bar_chart=pygal.Bar() 
        bar_chart.title = 'Employee grades  average per quarter'
    
       
        data = defaultdict(list)
        for empSkill in Employee.empSkills(self):
            data[str(empSkill.year) + " Q"+ str(empSkill.quarter)].append(empSkill.grade)
        
        for key,value in data.items():
            bar_chart.add(key, numpy.mean(value)) 
            
        # Add data to chart
        
           
       
        return mark_safe('<img src="%s" width="750" height="550" />' % (bar_chart.render_data_uri()))
    
    
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
    
    def get_data(self):
        """ 
        Fake Method to generate random data.
        In the real case, this method should arrange
        data to be plotted according to model instance
        fields' values.
        """
        return random_sample(5)

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
     
    def get_data(self):
        """ 
        Fake Method to generate random data.
        In the real case, this method should arrange
        data to be plotted according to model instance
        fields' values.
        """
        return random_sample(5) 
     
 
        
  
class CustomModelAdmin(admin.ModelAdmin):
   def __init__(self, model, admin_site):
    self.list_display = [field.name for field in model._meta.fields ]
    self.list_select_related: [x.name for x in model._meta.fields if isinstance(x, (models.ManyToOneRel, models.ForeignKey, models.OneToOneField,))]
    self.readonly_fields=['get_data']
    super(CustomModelAdmin, self).__init__(model, admin_site)
   
   

   



        
        
        



