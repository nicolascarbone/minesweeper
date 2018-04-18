
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Element
from .serializers import ElementSerializer


class ElementViewSet(viewsets.ModelViewSet):
    """
    Returns a list of all authors.
    """
    queryset = Element.objects.all()
    serializer_class = ElementSerializer

    # Set flag to element (PUT)
    def update(self, request, pk=None):
        element = self.get_queryset().get(pk=pk)
        element.set_as_flagged()
        serializer = self.get_serializer(element)
        return Response(serializer.data)
