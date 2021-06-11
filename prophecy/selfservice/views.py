from django.shortcuts import render
from rest_framework import viewsets
from selfservice.serializers import WinnerSerializer
from selfservice.models import Winner
# Create your views here.

class WinnerViewSet(viewsets.ModelViewSet):
    queryset =  Winner.objects.all().order_by("date")
    serializer_class = WinnerSerializer