import random

from rest_framework import viewsets
from rest_framework.response import Response

from .models import Grid
from .serializers import GridSerializer

from elements.models import Element


class GridViewSet(viewsets.ModelViewSet):
    """
    Returns a list of all authors.
    """
    queryset = Grid.objects.all()
    serializer_class = GridSerializer

    def create(self, request):

        rows = int(request.data.get('rows', 5))
        cells = int(request.data.get('cells', 5))
        mines = int(request.data.get('mines', 3))

        grid = Grid(rows=rows, cells=cells, mines=mines)
        grid.save()

        # Initialize elements with a 0 in each position
        elements = [[0] * cells for i in range(rows)]

        # set a few of random mines
        mines_count = 0
        
        while mines_count < mines:

            for mine in range(mines):
                x, y = random.randrange(0, rows), random.randrange(0, cells)
                if elements[x][y] == 0:
                    elements[x][y] = 1
                    mines_count = mines_count + 1

                # Stop if we reach our mines limit
                if mines_count >= mines:
                    break

        # Create elements
        elements_to_save = []
        for index, row in enumerate(elements):
            for element in row:
                elements_to_save.append(Element(grid=grid, is_bomb=element))

        Element.objects.bulk_create(elements_to_save)
        return Response()
