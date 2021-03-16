from django.urls import path

from . import views

app_name = 'hours'

urlpatterns = [
    path('', views.home, name='home',),
    path('hours-worked/', views.hours_worked, name='hours_worked',),
    path('updating-hours-worked/<int:hours_id>/', views.updating_hours_worked, name='updating_hours_worked',),
]
