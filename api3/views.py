from django.shortcuts import render
from rest_framework import viewsets

from api3.models import Reserva
from api3.serializers import ReservaSerializer


class ImovelViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
