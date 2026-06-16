from rest_framework import serializers
from .models import TecherModel

class TecherSerializer(serializers.ModelSerializer):
    class Meta:
        model = TecherModel
        fields = ('id', 'name', 'surname', 'birthday', 'ade', 'username', 'email')
