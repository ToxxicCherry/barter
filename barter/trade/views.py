from rest_framework.response import Response
from rest_framework.views import APIView

from .models import TradeOffer
from .serializers import TradeOffersSerializer

# Create your views here.


class TradeOffersView(APIView):
    def get(self, request):
        offers = TradeOffer.objects.select_related('User', 'Item').values(
            'pk',
            'user__pk',
            'user__username',
            'title',
            'description',
            'items_offered__pk',
            'items_offered__name',
            'items_offered__description',
            'items_offered_quantity',
            'items_requested__pk',
            'items_requested__name',
            'items_requested_quantity',
            'created_at'
        )
        return Response({'offers': TradeOffersSerializer(offers, many=True).data})