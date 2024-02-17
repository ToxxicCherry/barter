from django.urls import path, include, re_path
from .views import *


urlpatterns = [
    path('api/v1/offerslist/', TradeOffersView.as_view(), name='offerslist'),
    path('api/v1/user/inventory/', UserInventory.as_view()),
    path('api/v1/addoffer/', AddOffer.as_view()),
    path('api/v1/canceloffer/', CancelOffer.as_view()),
    path('api/v1/purchase/', Purchase.as_view()),
    re_path(r'^api/v1/auth/', include('djoser.urls')),
    re_path(r'^api/v1/auth/', include('djoser.urls.authtoken')),
]