import datetime
from django.db import models
from django.utils import timezone
# from __future__ import unicode_literals
#from django.utils.encoding import python_2_unicode_compatible


# Create your models here.
#@python_2_unicode_compatible

class Contato(models.Model):
    nome= models.CharField('Nome', max_length=50, unique=True)
    telefone= models.CharField('Telefone', max_length=15)
    data_criacao= models.DateTimeField('Data')
    data_atualizacao= models.DateTimeField('date updated')
    url = models.URLField()

    def was_published_recently(self):
        return self.data_criacao >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.nome