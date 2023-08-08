from django.db import models

# Create your models here.
class Editorial(models.Model):
    name = models.CharField(max_length = 25, verbose_name="Nombre")
    address = models.CharField(max_length = 150, verbose_name="Direccion")
    phone = models.CharField(max_length = 15, verbose_name="Numero de telefono")
    email = models.EmailField(max_length=50, verbose_name="Correo")
    web_site = models.CharField(max_length = 150, verbose_name="Sitio Web")
    
    def __str__(self):
        return self.name

    class Meta:
        managed = True
        verbose_name = 'Editorial'
