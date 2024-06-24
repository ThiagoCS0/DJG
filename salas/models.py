from django.db import models
class Salas(models.Model):
    sala=models.CharField(max_length=50, null=False, blank=False)
    inicio=models.DateTimeField(auto_now_add=True, null=False, blank=False)
    prazo=models.DateTimeField(null=False, blank=False)
    fim=models.DateTimeField(null=False)