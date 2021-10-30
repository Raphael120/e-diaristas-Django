from random import randint

from rest_framework import serializers
from web.models import Diarista


class DiaristaCidadeSerializer(serializers.ModelSerializer):
    reputacao = serializers.SerializerMethodField()
    
    class Meta:
        model = Diarista
        fields = ('nome_completo', 'foto_usuario', 'cidade', 'reputacao')
    
    def get_reputacao(self, obj):
        return randint(0, 5)
    