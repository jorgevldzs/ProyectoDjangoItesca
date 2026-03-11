from django.contrib import admin

# Register your models here.
from .models import Escuela, Maestro, Alumno
admin.site.register(Escuela)
admin.site.register(Maestro)
admin.site.register(Alumno)