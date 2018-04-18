from django.db import models

from grids.models import Grid


class Element(models.Model):
    grid = models.ForeignKey(Grid, related_name='elements', on_delete=models.CASCADE)
    is_bomb = models.BooleanField(default=False)
    row = models.PositiveSmallIntegerField(default=0)
    cell = models.PositiveSmallIntegerField(default=0)
    is_flagged = models.BooleanField(default=False)

    def __str__(self):
        return '{} - {}'.format(
            self.grid,
            self.pk)

    def set_as_flagged(self):
        self.is_flagged = True
        self.save()
