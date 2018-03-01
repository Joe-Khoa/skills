from django.contrib.auth.decorators import login_required
from django.shortcuts import render





# Create your views here.
@login_required
def my_view(reguest):
    return render(reguest,'home.html', context=None)


