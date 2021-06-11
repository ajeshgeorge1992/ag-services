from rest_framework import serializers

from selfservice.models import Winner

class WinnerSerializer(serializers.ModelSerializer):
    class Meta:
        model= Winner
        fields = '__all__'