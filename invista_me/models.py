from django.db import models
from datetime import datetime

# tabela banco de dados
class Investimento(models.Model):
  investimento = models.TextField(max_length=255)
  valor = models.FloatField()
  pago = models.BooleanField(default=False)
  data = models.DateField(default=datetime.now)
  
