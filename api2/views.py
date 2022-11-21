from django.shortcuts import render
from rest_framework import viewsets

from api2.models import Anuncio
from api2.serializers import AnuncioSerializer


class ImovelViewSet(viewsets.ModelViewSet):
    queryset = Anuncio.objects.all()
    serializer_class = AnuncioSerializer
