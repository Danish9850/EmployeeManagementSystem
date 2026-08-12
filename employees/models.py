from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    experience = models.CharField(max_length=50)
    salary = models.IntegerField()
    contact = models.CharField(max_length=15)
    
    # new field
    department = models.CharField(max_length=100)

    # Employee Photo
    photo = models.ImageField(
        upload_to='employee_photos/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name
    