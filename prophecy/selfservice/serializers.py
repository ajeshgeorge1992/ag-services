from rest_framework import serializers

from selfservice.models import Winner

class WinnerSerializer(serializers.HyperlinkedModelSerializer):
    class meta:
        model= Winner
        fields = '__all__'