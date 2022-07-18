from django.contrib import admin

# Register your models here.
from .models import RadarSensor


class RadarSensorAdmin(admin.ModelAdmin):
    search_fields = ['mac_address']


admin.site.register(RadarSensor, RadarSensorAdmin)
