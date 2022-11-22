from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import action

from api3.models import Reserva
from api3.serializers import ReservaSerializer


class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

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
