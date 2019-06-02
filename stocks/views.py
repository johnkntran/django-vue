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
