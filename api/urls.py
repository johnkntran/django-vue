from django.urls import include, path
from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register(r'stocks', views.StockViewSet)
router.register(r'portfolios', views.PortfolioViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('link/', views.add_stock_to_portfolio),
]
