from rest_framework import serializers
from .models import Chela


class ChelaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chela
        fields = '__all__'
