from django.shortcuts import render, redirect

from .models import HoursWorked
from .forms import HoursWorkedForm

"""Home view"""
def home(request):
    hours = HoursWorked.objects.all().order_by('-date_added')
    context= {'hours': hours}
    return render(request, 'hours/home.html', context)

def hours_worked(request):
    """adding a form"""
    if request.method != "POST":
        #blank form
        form = HoursWorkedForm()
    else:
        form = HoursWorkedForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hours:home')

    context = {'form': form}
    return render(request,'hours/hours_worked.html', context)
