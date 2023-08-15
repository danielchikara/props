from rest_framework import serializers
from .models import *

class InventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'