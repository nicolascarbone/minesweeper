from datetime import datetime

from django.db import models


class Grid(models.Model):
    rows = models.PositiveSmallIntegerField(default=5)
    cells = models.PositiveSmallIntegerField(default=5)
    mines = models.PositiveSmallIntegerField(default=3)
    datetime = models.DateTimeField(default=datetime.now)
