from django.db import models
from applications.editorial.models import Editorial
from applications.author.models import Author

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length = 25, verbose_name="Nombre")
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE, verbose_name="Editorial")
    author = models.ManyToManyField(Author, verbose_name="Autor")
    sipnosis = models.TextField()
    pub = models.DateField(auto_now=False, auto_now_add=False)
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)

    
    def __str__(self):
        return self.title

    class Meta:
        managed = True
        verbose_name = 'Book'