from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import ProjectWorked, TrackingHours
from .forms import ProjectWorkedForm, TrackingHoursForm

"""Home view"""
def home(request):
    projects = ProjectWorked.objects.all()

    if request.method != "POST":
        #show hours worked form
        form = TrackingHoursForm()

    else:
        form = TrackingHoursForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context= {'projects': projects, 'form': form}
    return render(request, 'hours/home.html', context)

def project_worked(request):
    """adding a form"""
    if request.method != "POST":
        #blank form
        form = ProjectWorkedForm()
    else:
        form = ProjectWorkedForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hours:home')

    context = {'form': form}
    return render(request,'hours/project_worked.html', context)

def updating_project_worked(request, project_id):
    project = get_object_or_404(ProjectWorked, id=project_id)
    if request.method != "POST":
        #show hours_worked info
        form = ProjectWorkedForm(instance=project)

    else:
        #updating info
        form = ProjectWorkedForm(request.POST, instance=project)

        if form.is_valid():
            form.save()
            messages.success(request, f'You have updated the information.')
            return redirect('hours:home')

    context = {'project': project, 'form': form}
    return render(request, 'hours/updating_project_worked.html', context)


def edit_trackinghours(request, hours_id):
    hours = get_object_or_404(TrackingHours, id=hours_id)
    if request.method !="POST":
        #show hours already logged
        form = TrackingHoursForm(instance=hours)

    else:
        #updating hours worked
        form = TrackingHoursForm(request.POST, instance=hours)
        if form.is_valid():
            form.save()
            return redirect('hours:home')

def delete_trackinghours(request, hours_id):
    hours = get_object_or_404(TrackingHours, id=hours_id)

    if request.method == "POST":
        hours.delete()
        context={'hours':hours}
        return redirect('hours:home')
