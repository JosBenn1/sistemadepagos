from django.contrib import admin
from .models import Pago

class PagoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Pago, PagoAdmin)