from django.db import models
import datetime

#Adding new projects or training
class HoursWorked(models.Model):
    title = models.CharField(max_length=200)
    project_status = [
        ('Open', 'Open'),
        ('Closed', 'Closed'),
        ('Training', 'Training'),
    ]
    status = models.CharField(max_length=10, choices=project_status, default='Open')
    languages = [
        ('Python', 'Python'),
        ('JavaScript', 'JavaScript')
    ]
    code_language = models.CharField(max_length=10, choices=languages, default='Python')
    hours_worked_in_day = models.IntegerField(default=1)
    date_added = models.DateField(help_text = 'Please use the following format: <em>YYYY-MM-DD</em>')

    class Meta:
        verbose_name_plural = "hours worked"

    def __str__(self):
        return self.title
