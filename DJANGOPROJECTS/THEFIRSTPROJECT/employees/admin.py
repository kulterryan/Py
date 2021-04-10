from django.contrib import admin
from .models import Employeer, AvailableJobs

# Register your models here.
@admin.register(Employeer)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email_id', 'phone_num']

@admin.register(AvailableJobs)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name']