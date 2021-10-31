from django.db import models


class Stock(models.Model):

    class ExchangeChoices(models.TextChoices):
        NASDAQ = 'NASDAQ', 'NASDAQ'
        NYSE = 'NYSE', 'NYSE'
        NYSE_ARCA = 'NYSE_ARCA', 'NYSE_ARCA'
        NYSE_AM = 'NYSE_AM', 'NYSE_AM'
        OTC = 'OTC', 'OTC'
        AMEX = 'AMEX', 'AMEX'

    exchange = models.CharField(max_length=10, choices=ExchangeChoices.choices, default=ExchangeChoices.NASDAQ)
    symbol = models.CharField(max_length=5)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'#{self.id} {self.name}'


class Portfolio(models.Model):
    name = models.CharField(max_length=100)
    stocks = models.ManyToManyField(Stock, related_name='portfolios')

    def __str__(self):
        return f'#{self.id} {self.name}'
