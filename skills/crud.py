from crudbuilder.abstract import BaseCrudBuilder
from .models import EmpSkills

class EmpSkillsCrud(BaseCrudBuilder):
    model=EmpSkills
    search_fields = ['employee__name']
    tables2_fields = ('year', 'quarter','employee','skill','grade')
    tables2_css_class = "table table-bordered table-condensed"
    tables2_pagination = 5  # default is 10
    modelform_excludes = ['id']
    login_required=True
    permission_required=True

    @classmethod
    def custom_queryset(cls, request, **kwargs):
        """Define your own custom queryset for list view"""
        qset = cls.model.objects.all()
        return qset

    @classmethod
    def custom_context(cls, request, context, **kwargs):
        """Define your own custom context for list view"""
        context['custom_data'] = "Some custom data"
        return context