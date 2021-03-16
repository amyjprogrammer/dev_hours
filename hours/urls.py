from django.urls import path

from . import views

app_name = 'hours'

urlpatterns = [
    path('', views.home, name='home',),
    path('project-worked/', views.project_worked, name='project_worked',),
    path('updating-project-worked/<int:project_id>/', views.updating_project_worked, name='updating_project_worked',),
]
