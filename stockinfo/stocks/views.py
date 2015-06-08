from django.shortcuts import render

from rest_framework import viewsets

from stockinfo.stocks.models import Stock
from stockinfo.stocks.serializers import StockSerializer


class StockViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows stocks to be searched.
    """
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
