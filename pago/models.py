from django.db import models

class Pago(models.Model):
    periodo = models.CharField(
        max_length=30,
        verbose_name="Periodo escolar")
    date = models.DateField(
        verbose_name="Fecha")
    created = models.DateTimeField(
        auto_now_add=True, 
        verbose_name="Fecha de creación")
    updated = models.DateTimeField(
        auto_now=True, 
        verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "pago"
        verbose_name_plural = "pagos"
        ordering = ['-created']

    def __str__(self):
        return self.created