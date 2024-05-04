from django.contrib import admin
from .models import Department,Designation,Employee,JobDescription,Location
# Register your models here.
admin.site.register(Department)
admin.site.register(Designation)
admin.site.register(Employee)
admin.site.register(JobDescription)
admin.site.register(Location)