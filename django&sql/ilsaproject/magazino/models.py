from _typeshed import Self
from django.db import models

# Create your models here.
class fabrica(models.Model):
    codice = models.CharField(max_length=10)
    materiale = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.materiale} ({self.codice})"

class magazino(models.Model):
    armadi = models.ForeignKey(fabrica, )
    cruscotto = models.IntegerField()
    quantita = models.IntegerField()

    def __str__(self):
        return f"{self.id}, {self.armadi} to {self.quantita}"
    
