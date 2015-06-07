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
