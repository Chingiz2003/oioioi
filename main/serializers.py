from rest_framework import serializers
from .models import *

class MarkModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarkModel
        fields = '__all__'