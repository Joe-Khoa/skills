from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def my_view(reguest):
    return render(reguest,'home.html', context=None)