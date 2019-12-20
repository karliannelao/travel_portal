from django.contrib import admin
from .models import Employee


# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'position', 'email')

admin.site.register(Employee, EmployeeAdmin)