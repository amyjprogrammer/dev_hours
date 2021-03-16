from django import forms

from .models import ProjectWorked, TrackingHours

class ProjectWorkedForm(forms.ModelForm):
    class Meta:
        model = ProjectWorked
        fields = '__all__'

class TrackingHoursForm(forms.ModelForm):
    class Meta:
        model = TrackingHours
        fields = ['hours_worked_in_day', 'date_added']
