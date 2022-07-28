from django.db import models

# Create your models here.


class Persona(models.Model):
    document = models.FloatField()
    description = models.CharField(max_length=40)
    date = models.DateField(auto_now_add=True, null=True,blank=True)