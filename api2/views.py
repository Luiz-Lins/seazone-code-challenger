from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import action

from api2.models import Anuncio
from api2.serializers import AnuncioSerializer


class AnuncioViewSet(viewsets.ModelViewSet):
    queryset = Anuncio.objects.all()
    serializer_class = AnuncioSerializer

    @action(detail=True, methods=['get'])
    def get(self, request):
        return HttpResponse('ok')

    @action(detail=True, methods=['post'])
    def post(self, request):
        return HttpResponse('ok')

    @action(detail=True, methods=['put'])
    def put(self, request, pk=None):
        return HttpResponse('ok')

    @action(detail=True, methods=['patch'])
    def patch(self, request, pk=None):
        return HttpResponse('ok')

    @action(detail=True, methods=['delete'])
    def delete(self, request, pk=None):
        return HttpResponse(status=204)
