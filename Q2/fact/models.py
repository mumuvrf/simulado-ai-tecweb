from django.db import models

# Create your models here.
class Fact(models.Model):
    descricao = models.TextField(max_length=500)
    curtidas = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.descricao} ({self.curtidas})"