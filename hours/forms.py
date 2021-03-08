from django import forms

from .models import HoursWorked

class HoursWorkedForm(forms.ModelForm):
    class Meta:
        model = HoursWorked
        fields = '__all__'
