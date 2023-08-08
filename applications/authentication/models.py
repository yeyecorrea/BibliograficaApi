from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Usuario", related_name="userprofile")
    name = models.CharField(max_length = 100)
    age = models.IntegerField(verbose_name="Edad", null=True)
    avatar = models.ImageField(verbose_name="Foto de perfil", upload_to=None, height_field=None, width_field=None, max_length=None, null=True)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        return self.user.username

