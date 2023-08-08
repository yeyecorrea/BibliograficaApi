from django.db import models
from applications.book.models import Book
from applications.author.models import Author
from .validators import *
# Create your models here.
class BinnacleState(models.Model):
    name = models.CharField(max_length = 25, verbose_name="Nombre")
    
    def __str__(self):
        return self.name

    class Meta:
        managed = True
        verbose_name = 'BinnacleState'
        
class BinnacleProgres(models.Model):
    initial_date = models.DateField(auto_now=False, auto_now_add=False)
    final_date = models.DateField(auto_now=False, auto_now_add=False)
    
    def __str__(self):
        return self.initial_date

    class Meta:
        managed = True
        verbose_name = 'BinnacleProgres'
        
class BinnacleQualification(models.Model):
    content = models.IntegerField(default=0, verbose_name="Contenido", validators=[validate_value])
    writing = models.IntegerField(default=0, verbose_name="Escritura", validators=[validate_value])
    dising = models.IntegerField(default=0, verbose_name="Diseño", validators=[validate_value])
    
    def __str__(self):
        return "Calificacion"

    class Meta:
        managed = True
        verbose_name = 'BinnacleQualification'

class Binnacle(models.Model):
    title = models.CharField(max_length = 150, verbose_name="Titulo")
    book = models.OneToOneField(Book, on_delete=models.CASCADE, verbose_name="Libro")
    author = models.OneToOneField(Author, on_delete=models.CASCADE, verbose_name="Author")
    state = models.OneToOneField(BinnacleState, on_delete=models.CASCADE, verbose_name="Estado")
    progres = models.OneToOneField(BinnacleProgres, on_delete=models.CASCADE, verbose_name="Progreso")
    phrase = models.TextField(verbose_name="Frases")
    commet = models.TextField(verbose_name="Comentarios")
    qualification = models.OneToOneField(BinnacleQualification, on_delete=models.CASCADE, verbose_name="Calificacion")
    buy = models.DateField(auto_now=False, auto_now_add=False, verbose_name="Fecha de compra")
    
    def __str__(self):
        return self.title

    class Meta:
        managed = True
        verbose_name = 'Binnacle'
