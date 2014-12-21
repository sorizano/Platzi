from django.db import models

# Create your models here.
class Preguntas(models.Model):
	titulo = models.CharField(max_length=255)

class Respuestas(models.Model):
	titulo = models.CharField(max_length=255)
	pregunta = models.ForeignKey(Preguntas)