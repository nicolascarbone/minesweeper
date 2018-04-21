from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from rest_framework import serializers, exceptions

from .models import Grid
from elements.serializers import ElementSerializer


class GridSerializer(serializers.ModelSerializer):
    # elements = ElementSerializer(many=True, read_only=True)

    class Meta:
        model = Grid
        fields = ('pk', 'rows', 'cells', 'mines', 'datetime')
