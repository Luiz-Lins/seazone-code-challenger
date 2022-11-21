from django.shortcuts import render
from rest_framework import viewsets
from api1.models import Imovel
from api1.serializers import ImovelSerializer


class ImovelViewSet(viewsets.ModelViewSet):
    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializer
