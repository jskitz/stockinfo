import csv

from django.conf import settings
from django.core.management import BaseCommand, CommandError

from stockinfo.stocks.models import Stock


class Command(BaseCommand):
    def handle(self, *args, **options):
        fieldnames = ('symbol', 'name', 'last_sale', 'market_cap', 'ipo_year', 'sector',
            'industry', 'summary_quote') 

        stock_data = []
        with open(settings.BASE_DIR + '/stockinfo/stocks/data/amex.csv') as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=fieldnames)
            next(reader) # increment by 1 to skip header
            for row in reader:
                stock_data.append(row)

        with open(settings.BASE_DIR + '/stockinfo/stocks/data/nasdaq.csv') as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=fieldnames)
            next(reader) # increment by 1 to skip header
            for row in reader:
                stock_data.append(row)

        with open(settings.BASE_DIR + '/stockinfo/stocks/data/nyse.csv') as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=fieldnames)
            next(reader) # increment by 1 to skip header
            for row in reader:
                stock_data.append(row)

        for stock in stock_data:
            print 'working on ticker symbol %s' % stock['symbol']
            _stock, created = Stock.objects.get_or_create(symbol=stock['symbol'].strip())
            _stock.name = stock['name'].strip()
            if not stock['last_sale'].strip() == 'n/a':
                _stock.last_sale = float(stock['last_sale'])
            _stock.market_cap = stock['market_cap'].strip()
            _stock.ipo_year = stock['ipo_year'].strip()
            _stock.sector = stock['sector'].strip()
            _stock.industry = stock['industry'].strip()
            _stock.summary_quote = stock['summary_quote'].strip()
            _stock.save()

        print 'total number of stocks imported: %d' % len(stock_data)
