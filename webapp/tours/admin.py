from django.contrib import admin
from .models import Tour

# Register your models here.


class TourAdmin(admin.ModelAdmin):
    list_display = (
        'start_date',
        'end_date',
        'mode_of_travel',
        'ticket_cost',
        'approving_manager',
        'status',
        'created_by',
        'modified_date')


admin.site.register(Tour, TourAdmin)
