from django.db import models
from django.db.models import Sum, F, FloatField
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db.models.signals import m2m_changed

# Create your models here.
class Alunos (models.Model):
    nome = models.CharField(max_length = 30)
    sobrenome = models.CharField (max_length = 30)
    nota1 = models.DecimalField( max_digits=3, decimal_places=1, null=True, blank = True)
    nota2 = models.DecimalField( max_digits=3, decimal_places=1, null=True, blank = True)
    nota3 = models.DecimalField( max_digits=3, decimal_places=1, null=True, blank = True)
    media = models.DecimalField( max_digits=3, decimal_places=1, null =True, blank = True)
    idade = models.IntegerField()
    obs = models.TextField()
    
    def calcular_media(self):
        media_calc = (float(self.nota1) + float(self.nota2) + float(self.nota3))/3
        self.media = media_calc
        #self.save
        Alunos.objects.filter(id=self.id).update(media=media_calc)

    def __str__ (self):
        return self.nome + ' ' + self.sobrenome

@receiver (post_save, sender = Alunos)
def update_media (sender, instance, **kwargs):
    instance.calcular_media()