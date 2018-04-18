from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from rest_framework import serializers, exceptions

from .models import Element


class ElementSerializer(serializers.ModelSerializer):

    clean_adjacents = serializers.SerializerMethodField()

    def get_clean_adjacents(self, obj):
        return '{}, {}'.format(obj.row, obj.cell)

    class Meta:
        model = Element
        fields = (
            'grid', 'row', 'cell',
            'is_bomb', 'is_flagged', 'clean_adjacents'
        )
