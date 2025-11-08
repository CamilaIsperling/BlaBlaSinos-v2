from django.db import models

class Carona(models.Model):
    origem = models.CharField(max_length=120)
    destino = models.CharField(max_length=120)
    horario = models.DateTimeField()
    vagas = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.origem} → {self.destino} ({self.vagas} vagas)"
