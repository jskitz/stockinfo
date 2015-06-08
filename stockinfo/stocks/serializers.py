from rest_framework import serializers

from stockinfo.stocks.models import Stock


class StockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stock
        fields = ('id', 'symbol', 'name')


class StockHistorySerializer(serializers.Serializer):
    date = serializers.DateField()
    opened_at = serializers.FloatField()
    closed_at = serializers.FloatField()
    high = serializers.FloatField()
    low = serializers.FloatField()
    average = serializers.FloatField()
