from rest_framework.response import Response
from rest_framework.views import APIView
from .services import *
from .serializers import *
# Create your views here.


class TradeOffersView(APIView):
    def get(self, _):
        return Response({'offers': TradeOffersSerializer(get_offers(), many=True).data})


class UserInventory(APIView):

    def get(self, request, user_id):

        return Response({'response': get_users_inventory(user_id)})


class AddOffer(APIView):
    def post(self, request):
        data = AddOfferSerializer(data=request.data)
        if data.is_valid():
            return Response({'response': addoffer(data.validated_data)})
        return Response({'response': 'invalid data'})


class CancelOffer(APIView):
    def post(self, request):
        serialized_data = CancelOfferSerializer(data=request.data)
        if serialized_data.is_valid():
            canceloffer(
                user_id=serialized_data.validated_data.get('user_id'),
                offer_id=serialized_data.validated_data.get('offer_id'),
                item_id=serialized_data.validated_data.get('item_offered_id'),
                item_quantity=serialized_data.validated_data.get('item_offered_quantity')
            )
            return Response({'response': 'success'})
        return Response({'response': 'invalid data'})