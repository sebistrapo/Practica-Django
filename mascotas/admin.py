from django.contrib import admin
from django.utils.html import format_html

# Register your models here.

from .models import *

@admin.register(Mascotas)
class MascotasAdmin(admin.ModelAdmin):
    list_display = ["id_mascota", "nombre", "raza", "edad"]
    list_filter = ["nombre", "raza", "edad"]

@admin.register(Usuarios)
class UsersAdmin(admin.ModelAdmin):
    list_display = ["id_user", "user", "clave"]
    list_filter = ["id_user", "user", "clave"]