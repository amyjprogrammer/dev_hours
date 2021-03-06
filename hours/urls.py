from django.urls import path

from . import views

app_name = 'hours'

urlpatterns = [
    path('', views.home, name='home',),
    path('project-worked/', views.project_worked, name='project_worked',),
    path('updating-project-worked/<int:project_id>/', views.updating_project_worked, name='updating_project_worked',),
    path('edit-hours/<int:hours_id>/', views.edit_trackinghours, name='edit_trackinghours',),
    path('delete-hours/<int:hours_id>/', views.delete_trackinghours, name='delete_trackinghours',),
    path('add-hours/<int:project_id>/', views.add_trackinghours, name='add_trackinghours',),
]
