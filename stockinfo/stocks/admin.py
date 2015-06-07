from django.contrib import admin

from stockinfo.stocks.models import Stock


class StockAdmin(admin.ModelAdmin):
    list_display = ('symbol', 'name', 'market_cap', 'ipo_year', 'summary_quote')
    search_fields = ('symbol', 'name')

admin.site.register(Stock, StockAdmin)
