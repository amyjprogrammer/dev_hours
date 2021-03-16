from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

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

def updating_hours_worked(request, hours_id):
    hours = get_object_or_404(HoursWorked, id=hours_id)
    if request.method != "POST":
        #show hours_worked info
        form = HoursWorkedForm(instance=hours)

    else:
        #updating info
        form = HoursWorkedForm(request.POST, instance=hours)

        if form.is_valid():
            form.save()
            messages.success(request, f'You have updated the information.')
            return redirect('hours:home')

    context = {'hours': hours, 'form': form}
    return render(request, 'hours/updating_hours_worked.html', context)
