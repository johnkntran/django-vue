from django.db import models


class Stock(models.Model):
    """
    An example of a stock model to represent some stock tickers and their data.
    """
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=5)
    exchange = models.CharField(max_length=10, choices=(
        ('NYSE', 'New York Stock Exchange'),
        ('NASDAQ', 'Nasdaq Exchange')
    ))
    active = models.BooleanField(default=True)
    price = models.FloatField() # FloatField for convenience, use DecimalField in real life
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '#{} {}'.format(self.id, self.name)


class Portfolio(models.Model):
    """
    An example of someone's portfolio containing some stocks.
    """
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=25)
    stocks = models.ManyToManyField(Stock)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
