from django.urls import path
from .views import *


urlpatterns = [
    path('api/v1/offerslist', TradeOffersView.as_view())
]