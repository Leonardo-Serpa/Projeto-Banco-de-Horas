from django.db import models
from datetime import datetime

# Create your models here.
class Funcionarios(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    hora = models.DateTimeField(auto_now_add=True)
