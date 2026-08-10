from django.db import models

# Create your models here.

class Usuarios(models.Model):
    id_user = models.CharField(unique=True, primary_key=True)
    user = models.CharField(unique=True, null=False, max_length=254)
    clave = models.CharField(null=False, max_length=254)

    def __str__(self):
        return f"Usuario: {self.user} - Clave: {self.clave}"

class Mascotas(models.Model):
    id_mascota = models.IntegerField(unique=True, primary_key=True)
    nombre = models.CharField(max_length=100, default="N/A", null=True)
    raza = models.CharField(max_length=100, null=False)
    edad = models.IntegerField(null=False)

    def __str__(self):
        return f"Nombre: {self.nombre} - Raza: {self.raza} - Edad: {self.edad}"