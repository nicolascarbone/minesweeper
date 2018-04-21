import random
import datetime

from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response

from .models import Grid
from .serializers import GridSerializer

from elements.serializers import ElementSerializer

from elements.models import Element


class GridViewSet(viewsets.ModelViewSet):
    """
    Returns a list of all authors.
    """
    queryset = Grid.objects.all()
    serializer_class = GridSerializer

    def get(self, request, pk=None):
        grid = get_object_or_404(Grid, pk=pk)
        serializer = self.get_serializer(grid)
        return Response(serializer.data)

    def get_older_games(self, request):
        qs = self.get_queryset()
        older = qs.filter(user=request.user)
        serializer = self.get_serializer(older, many=True)
        return Response(serializer.data)

    def explore(self, request, grid, row, cell):
        grid = get_object_or_404(Grid, pk=grid)
        element = grid.elements.get(row=row, cell=cell)
        serializer = ElementSerializer(element)
        return Response(serializer.data)

    def delete(self, request, pk=None):
        grid = get_object_or_404(Grid, pk=pk)
        grid.delete()
        return Response()

    def create(self, request):

        rows = int(request.data.get('rows', 5))
        cells = int(request.data.get('cells', 5))
        mines = int(request.data.get('mines', 3))

        # Create a new grid
        grid = Grid(user=request.user, rows=rows, cells=cells, mines=mines)
        grid.save()

        # Initialize elements with a 0 in each position
        # Rows and Cells will starts at position 1
        elements = [[0] * cells for i in range(rows)]

        # set up a few random bombs according to the specified mines
        mines_count = 0

        while mines_count < mines:

            # We just need to save bomb elements they are enough to
            # recreate a grid having the number of cells and rows
            for mine in range(mines):

                # Rows and Cells will starts at position 1
                x, y = random.randrange(0, rows), random.randrange(0, cells)

                if elements[x][y] == 0:
                    elements[x][y] = 1
                    mines_count = mines_count + 1

                # Stop if we reach our mines limit
                if mines_count >= mines:
                    break

        # Create elements
        elements_to_save = []
        for row, cells in enumerate(elements):
            for cell, is_bomb in enumerate(cells):
                elements_to_save.append(Element(
                    grid=grid,
                    is_bomb=is_bomb,
                    row=row,
                    cell=cell))

        saved = Element.objects.bulk_create(elements_to_save)

        serializer = self.get_serializer(grid)
        return Response(serializer.data)
