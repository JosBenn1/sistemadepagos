from django.db import models

class Estudiante(models.Model):
    matricula = models.IntegerField(
        verbose_name= "Matricula")
    name = models.CharField(
        max_length=30,
        verbose_name= "Nombre")
    lastname = models.CharField(
        max_length=50,
        verbose_name="Apellidos")
    email = models.EmailField(
        verbose_name= "Correo electronico")
    password = models.CharField(
        max_length= 8,
        verbose_name= "Contraseña")
    image = models.ImageField(
        upload_to="perfiles",
        verbose_name="Foto de perfil")   
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha de creación")
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name="Fecha de edición")

    class Meta:
        verbose_name = 'Alumno'
        verbose_name_plural = 'Alumnos'
        ordering = ["-created"]

    def __str__(self):
        return self.name