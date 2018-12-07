from django.db import models

# Create your models here.
class Alunos (models.Model):
    nome = models.CharField(max_length = 30)
    sobrenome = models.CharField (max_length = 30)
    nota1 = models.DecimalField( max_digits=3, decimal_places=1)
    nota2 = models.DecimalField( max_digits=3, decimal_places=1)
    nota3 = models.DecimalField( max_digits=3, decimal_places=1)
    media = models.DecimalField( max_digits=3, decimal_places=1)
    idade = models.IntegerField()
    obs = models.TextField()
    
        
    def __str__ (self):
        return self.nome + ' ' + self.sobrenome


