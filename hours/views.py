from django.shortcuts import render

from .models import HoursWorked
from .forms import HoursWorkedForm

"""Home view"""
def home(request):
    context= {}
    return render(request, 'hours/home.html', context)
