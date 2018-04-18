from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from rest_framework import serializers, exceptions

from .models import Grid


class GridSerializer(serializers.ModelSerializer):
    elements = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Grid
        fields = ('rows', 'cells', 'mines', 'datetime', 'elements')
