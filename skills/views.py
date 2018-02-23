from django.shortcuts import render

# Create your views here.
def my_view(reguest):
    return render(reguest,'index.html', context=None)