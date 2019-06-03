from django.urls import path, include
from stocks.views import Stocks, Portfolios, add_stock_to_portfolio, remove_stock_from_portfolio, index


urlpatterns = [
    path('', Stocks.as_view()),
    path('portfolios/', Portfolios.as_view()),
    path('add_stock_to_portfolio/', add_stock_to_portfolio),
    path('remove_stock_from_portfolio/', remove_stock_from_portfolio),
    path('example/', index),
]
