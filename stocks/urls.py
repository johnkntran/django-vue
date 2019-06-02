from django.urls import path, include
from stocks.views import Stocks, Portfolios


urlpatterns = [
    path('', Stocks.as_view()),
    path('portfolios/', Portfolios.as_view()),
]
