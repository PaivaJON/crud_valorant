from django.shortcuts import render
from rest_framework import viewsets
from .models import Mapa
from .serializers import MapaSerializer

class MapaViewSet(viewsets.ModelViewSet):
    queryset = Mapa.objects.all()
    serializer_class = MapaSerializer
