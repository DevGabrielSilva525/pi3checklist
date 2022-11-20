from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Usuarios(models.Model):
    usuario = models.OneToOneField(User, related_name='profile')
    img_perfil = models.FileField()