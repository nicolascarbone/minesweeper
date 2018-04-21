from datetime import datetime

from django.db import models
from django.contrib.auth.models import User


class Grid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rows = models.PositiveSmallIntegerField(default=5)
    cells = models.PositiveSmallIntegerField(default=5)
    mines = models.PositiveSmallIntegerField(default=3)
    datetime = models.DateTimeField(default=datetime.now)
    finished = models.BooleanField(default=False)
