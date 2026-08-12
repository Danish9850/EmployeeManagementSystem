from django.db import models
from employees.models import Employee

# Create your models here.
class Leave(models.Model):
  LEAVE_TYPES = [    
    ("Sick", "Sick"),
    ("Casual", "Casual"),
    ("Annual", "Annual"),
    ("Earned", "Earned"),
    ("Maternity", "Maternity"),
    ("Paternity", "Paternity"),
    ("Other", "Other"),
  ]

  STATUS = (
    ("Pending", "Pending"),
    ("Approved", "Approved"),
    ("Rejevted", "Rejected"),
  )

  employee = models.ForeignKey(
    Employee,
    on_delete=models.CASCADE
  )

  leave_type = models.CharField(
    max_length=20,
    choices=LEAVE_TYPES
  )

  start_date = models.DateField()

  end_date = models.DateField()

  reason = models.TextField()

  status = models.CharField(
    max_length=20,
    choices=STATUS,
    default="Pending"    
  )

  applied_on =models.DateTimeField(
    auto_now_add=True
  )

  def __str__(self):
    return f"{self.employee.name} - {self.leave_type}"

    
