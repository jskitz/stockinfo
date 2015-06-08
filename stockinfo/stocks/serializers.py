from rest_framework import serializers

from stockinfo.stocks.models import Stock


class StockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stock
        fields = ('symbol', 'name')

