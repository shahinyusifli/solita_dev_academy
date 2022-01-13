from django.contrib import admin
from .models import Farms


class FarmsAdmin(admin.ModelAdmin):
    list_display = ('location', 'date_time', 'sensor_type', 'values')

# Register your models here.
admin.site.register(Farms, FarmsAdmin)
