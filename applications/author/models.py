from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length = 50, verbose_name="Nombre")
    last_name = models.CharField(max_length = 50, verbose_name="Apellidos")
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, verbose_name="Imagen")
    biografia = models.TextField(verbose_name="Biografia")
    
    def __str__(self):
        return self.name

    class Meta:
        managed = True
        verbose_name = 'Autor'