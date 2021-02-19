from rest_framework import serializers

from .models import Victim_Request,Victim_Request_Status


class VictimRequestSerializer( serializers.ModelSerializer):
    class Meta:
        model = Victim_Request 
        fields = '__all__'

class VictimRequestStatusSerializer( serializers.ModelSerializer):
    class Meta:
        model = Victim_Request_Status
        fields = '__all__'