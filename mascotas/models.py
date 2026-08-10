from django.db import models

# Create your models here.

class Mascotas(models.Model):
    id_mascota = models.IntegerField(unique=True, primary_key=True)
    nombre = models.CharField(max_length=100, default="N/A")
    raza = models.CharField(max_length=100, null=True)
    edad = models.IntegerField(null=True)
    # ROLES = (
    #     ("cordi", "Cordinador"), 
    #     ("secre", "Secretaria"),
    #     ("profe", "Instructor"),
    #     ("aprdz", "Aprendiz"),
    # )
    # rol = models.CharField(choices=ROLES, max_length=10, default="aprdz")

    def __str__(self):
        return f"Nombre: {self.nombre} - Raza: {self.raza} - Edad: {self.edad}"