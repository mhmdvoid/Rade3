from rest_framework import serializers

from .models import Victim_Request 


class VictimRequestSerializer( serializers.ModelSerializer):
    class Meta:
        model = Victim_Request 
        fields = '__all__'