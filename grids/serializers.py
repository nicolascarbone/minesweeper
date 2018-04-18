from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from rest_framework import serializers, exceptions

from .models import Grid


class GridSerializer(serializers.ModelSerializer):

    class Meta:
        model = Grid
        # fields = ('first_name', 'last_name', 'fullname')
