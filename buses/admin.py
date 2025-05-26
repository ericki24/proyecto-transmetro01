from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Bus

@admin.register(Bus)
class BusAdmin(admin.ModelAdmin):
    list_display = ['id_bus', 'placa', 'capacidad', 'id_linea', 'id_parqueo']
