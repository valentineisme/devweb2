from django.db import models
from django.contrib.auth.models import User


class usuario(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, editable=False, on_delete=models.CASCADE)
    nome = models.CharField(max_length=128)
    sobrenome = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    senha = models.CharField(max_length=128, null=True)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.nome

# Create your models here.
