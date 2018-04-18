from django.db import models

from grids.models import Grid


class Element(models.Model):
    grid = models.ForeignKey(Grid, on_delete=models.CASCADE)
    is_bomb = models.BooleanField(default=False)
    # position = 
