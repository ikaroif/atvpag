from django.db import models

# Create your models here.

class Carro(models.Model):
    id_carro = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=100)
    modelo = models.CharField(max_length=50)
    cor = models.CharField(max_length=30)
    ano = models.IntegerField()

    def __str__(self):
        return f"{self.modelo} - {self.ano}"
