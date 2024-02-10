from django.urls import path
from .views import *


urlpatterns = [
    path('api/v1/offerslist', TradeOffersView.as_view()),
    path('api/v1/user/<int:user_id>/inventory/', UserInventory.as_view()),
    path('api/v1/addoffer/', AddOffer.as_view()),
    path('api/v1/canceloffer/', CancelOffer.as_view()),
    path('api/v1/purchase/', Purchase.as_view())
]