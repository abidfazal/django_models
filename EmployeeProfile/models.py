from django.db import models
from django.utils import timezone
# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.name


class JobDescription(models.Model):
    name = models.CharField(max_length=200)
    details = models.CharField(max_length=255)
    
    
class Designation(models.Model):
    name  = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    
    
class Department(models.Model):
    name = models.CharField(max_length=100)
    location = models.OneToOneField(Location, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name
    
class Employee(models.Model):
    name =  models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    cnic  = models.IntegerField()
    data_of_joining = models.DateField(default=timezone.now())
    department = models.OneToOneField(Department, on_delete= models.PROTECT)
    job_description = models.ForeignKey(JobDescription,on_delete=models.CASCADE)
    designation = models.ForeignKey(Designation, on_delete=models.PROTECT)