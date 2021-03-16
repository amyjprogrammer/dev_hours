from django.contrib import admin

# Register your models here.
from .models import ProjectWorked, TrackingHours

admin.site.register(ProjectWorked)
admin.site.register(TrackingHours)
