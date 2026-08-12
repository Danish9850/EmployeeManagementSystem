from django.db import models
from employees.models import Employee

# Create your models here.
class Task(models.Model):
    PRIORITY_CHOICES = [
        ('Low','Low'),
        ('Medium','Medium'),
        ('High','High'),
    ]

    STATUS_CHOICES = [
        ('Pending','Pending'),
        ('In Progress','In Progess'),
        ('Completed','Completed'),
    ]

    employee = models.ForeignKey(Employee,
on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    def __str__(self):
        return self.title
