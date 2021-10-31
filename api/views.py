from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_202_ACCEPTED

from .models import Stock, Portfolio
from .serializers import StockSerializer, PortfolioSerializer


class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all().order_by('symbol')
    serializer_class = StockSerializer


class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all().order_by('name')
    serializer_class = PortfolioSerializer


@api_view(['POST'])
def add_stock_to_portfolio(request):
    stock_id = request.data['stock_id']
    portfolio_id = request.data['portfolio_id']
    stock = Stock.objects.get(pk=stock_id)
    portfolio = Portfolio.objects.get(pk=portfolio_id)
    portfolio.stocks.add(stock)
    return Response(data='OK', status=HTTP_202_ACCEPTED)
