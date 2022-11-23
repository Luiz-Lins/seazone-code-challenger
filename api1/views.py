from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import action

from api1.models import Imovel
from api1.serializers import ImovelSerializer


class ImovelViewSet(viewsets.ModelViewSet):
    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializer

    # @action(detail=True, methods=['get'])
    # def get(self, request):
    #     return HttpResponse('ok')
    #
    # @action(detail=True, methods=['post'])
    # def post(self, request):
    #     return HttpResponse('ok')
    #
    # @action(detail=True, methods=['put'])
    # def put(self, request, pk=None):
    #     return HttpResponse('ok')
    #
    # @action(detail=True, methods=['patch'])
    # def patch(self, request, pk=None):
    #     return HttpResponse('ok')
    #
    # @action(detail=True, methods=['delete'])
    # def delete(self, request, pk=None):
    #     return HttpResponse('ok')
