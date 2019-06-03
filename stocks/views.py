from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from stocks.models import Stock, Portfolio
from stocks.serializers import StockSerializer, PortfolioSerializer


class Stocks(APIView):
    """
    View to list all stocks in the system.
    """

    def get(self, request, format='json'):
        """
        Return a list of all stocks.
        """
        stocks = Stock.objects.all().order_by('name')
        stock_serializer = StockSerializer(stocks, many=True)
        return Response(data=stock_serializer.data, status=status.HTTP_200_OK)


class Portfolios(APIView):
    """
    View to list all portfolios in the system.
    """

    def get(self, request, format='json'):
        """
        Return a list of all stocks.
        """
        portfolios = Portfolio.objects.all().order_by('name')
        portfolio_serializer = PortfolioSerializer(portfolios, many=True)
        return Response(data=portfolio_serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def add_stock_to_portfolio(request):
    """
    Add a specific stock (by symbol) to a portfolio (by slug).
    """
    stock_symbol = request.data['stock']
    portfolio_slug = request.data['portfolio']
    stock = Stock.objects.get(symbol=stock_symbol)
    portfolio = Portfolio.objects.get(slug=portfolio_slug)
    portfolio.stocks.add(stock)
    return Response(status=201)


@api_view(['POST'])
def remove_stock_from_portfolio(request):
    """
    Remove a specific stock (by symbol) to a portfolio (by slug).
    """
    stock_symbol = request.data['stock']
    portfolio_slug = request.data['portfolio']
    stock = Stock.objects.get(symbol=stock_symbol)
    portfolio = Portfolio.objects.get(slug=portfolio_slug)
    portfolio.stocks.remove(stock)
    return Response(status=204)


def index(request):
    context = {'portfolios': Portfolio.objects.all(), 'stocks': Stock.objects.all()}
    return render(request, 'stocks/index.html', context)
