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

    def save(self):
        if not self.id:
            c = usuario.objects.filter(email=self.email).count()
            if c:
                raise Exception("Email Existente")

            usr = User.objects.filter(username=self.email)
            if usr:
                u = usr[0]
            else:
                u = User.objects.create_user(self.email, self.email, self.senha)
            u.save()
            self.user = u
        else:
            self.user.username = self.email
            self.user.email = self.email
            self.user.set_password(self.senha)
            self.user.save()

        super(usuario, self).save()

    def __str__(self):
        return self.nome

# Create your models here.
