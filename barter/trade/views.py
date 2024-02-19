from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from .services import *
from .serializers import *
from barter.helper import query_debugger
# Create your views here.


class ItemsView(ListAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Item.objects.all()
    serializer_class = ItemsSerializer

    def get(self, _):
        queryset = self.get_queryset()
        serializer = ItemsSerializer(queryset, many=True)
        return Response(serializer.data)


class TradeOffersView(APIView):
    permission_classes = (IsAuthenticated, )

    @query_debugger
    def get(self, _):
        return Response({'offers': TradeOffersSerializer(get_offers(), many=True).data})


class UserInventory(APIView):
    permission_classes = (IsAuthenticated, )

    @query_debugger
    def get(self, request):
        return Response({
            'response':
                UserInventorySerializer(
                    get_users_inventory(request.user.id),
                    many=True
                ).data
        })


class AddOffer(APIView):
    permission_classes = (IsAuthenticated, )

    @query_debugger
    def post(self, request):
        serialized_data = AddOfferSerializer(data=request.data)
        if serialized_data.is_valid():
            return Response({'response': addoffer(serialized_data.validated_data, request.user.id)})
        return Response({'response': 'invalid data'})


class CancelOffer(APIView):
    permission_classes = (IsAuthenticated, )

    @query_debugger
    def post(self, request):
        serialized_data = CancelOfferSerializer(data=request.data)
        if serialized_data.is_valid():
            canceloffer(serialized_data.validated_data, request.user.id)
            return Response({'response': 'success'})
        return Response({'response': 'invalid data'})


class Purchase(APIView):
    permission_classes = (IsAuthenticated, )

    @query_debugger
    def post(self, request):
        serialized_data = PurchaseSerializer(data=request.data)
        if serialized_data.is_valid():
            return Response({
                'response': purchase(
                    serialized_data.validated_data,
                    request.user.id
                )
            })
        return Response({'response': 'invalid data'})