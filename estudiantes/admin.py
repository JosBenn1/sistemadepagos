from django.contrib import admin
from .models import Estudiante

class EstudianteAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Estudiante, EstudianteAdmin)