from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from rest_framework import serializers, exceptions

from .models import Grid
from elements.serializers import ElementSerializer


class GridSerializer(serializers.ModelSerializer):
    datetime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Grid
        fields = ('pk', 'rows', 'cells', 'mines', 'datetime')
