import django_tables2 as tables
from .models import EmpSkills


class EmpSkillsTable(tables.Table):

    class Meta:
        model =  EmpSkills
        attrs = {"class": "table table-bordered table-condensed"}