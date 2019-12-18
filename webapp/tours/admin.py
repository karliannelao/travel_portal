from django.contrib import admin
from .models import Employee, Tour

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'position', 'email')

class TourAdmin(admin.ModelAdmin):
    list_display = ('start_date', 'end_date', 'mode_of_travel', 'ticket_cost', 'approving_manager', 'status', 'created_by', 'modified_date')

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Tour, TourAdmin)
