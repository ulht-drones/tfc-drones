from django.db import models
import json

# Create models
class Celula (models.Model):
    nome = models.CharField(max_length=30)
    coordenadas = models.JSONField(default='')

    def __str__(self):
        return f'{self.coordenadas}'

    '''def __init__(self, lat, long):
        self.coordenadas = '{"type": "Feature", "geometry": {"type": "Point", "coordinates": [%f, %f]}}' %(lat,long)
'''

class AreaServico (models.Model):
    nome = models.CharField(max_length=30)
    coordenadas = models.JSONField(default='')


class Drone (models.Model):
    nome = models.CharField(max_length=30)
    coordenadas = models.JSONField(default='')
