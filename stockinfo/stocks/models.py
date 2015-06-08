from django.db import models

class Stock(models.Model):
    symbol = models.CharField(max_length=10, blank=False, unique=True)
    name = models.CharField(max_length=24, blank=False)
    last_sale = models.FloatField(blank=False, null=True)
    market_cap = models.CharField(max_length=12, blank=False)
    ipo_year = models.CharField(max_length=4, blank=False)
    sector = models.CharField(max_length=22, blank=False)
    industry = models.CharField(max_length=64, blank=False)
    summary_quote = models.URLField(blank=False)

    class Meta:
        pass

    def __unicode__(self):
        return self.symbol

class StockPrice(object):
    """
    Stock price objects are not stored in the database, and are just instantiated as prices
    are pulled from Yahoo.
    """
    def __init__(self, *args, **kwargs):
        self.symbol = kwargs['Symbol']
        self.date = kwargs['Date']
        self.opened_at = float(kwargs['Open'])
        self.low = float(kwargs['Low'])
        self.high = float(kwargs['High'])
        self.closed_at = float(kwargs['Close'])
        self.volume = int(kwargs['Volume'])
        self.average = (self.opened_at + self.low + self.high + self.closed_at) / 4.0
