from datetime import date, timedelta

from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from yahoo_finance import Share

from stockinfo.stocks.models import Stock, StockPrice
from stockinfo.stocks.serializers import StockSerializer, StockHistorySerializer


class StockViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows stocks to be searched.
    """
    queryset = Stock.objects.all().order_by('symbol')
    serializer_class = StockSerializer

    def list(self, request):
        stocks = Stock.objects.all().order_by('symbol')
        if 'q' in request.GET:
            stocks = Stock.objects.filter(symbol__istartswith=request.GET['q']).order_by('symbol')

        page = self.paginate_queryset(stocks)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(stocks, many=True)
        return Response(serializer.data)

    @list_route()
    def history(self, request):
        stocks = []
        if 'symbol' in request.GET:
            end = date.today()
            start = end - timedelta(days=31)  # at least a month of data
            stock = Share(request.GET['symbol'])
            stocks = stock.get_historical(str(start), str(end))
            stocks = [StockPrice(**s) for s in stocks]

        serializer = StockHistorySerializer(stocks, many=True)
        return Response(serializer.data)
