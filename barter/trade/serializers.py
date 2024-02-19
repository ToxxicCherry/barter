from rest_framework import serializers
from trade.models import Item


class TradeOffersSerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    user__pk = serializers.IntegerField()
    user__username = serializers.CharField()
    item_offered__pk = serializers.IntegerField()
    item_offered__name = serializers.CharField()
    item_offered__description = serializers.CharField()
    item_offered__image_url = serializers.URLField()
    item_offered_quantity = serializers.IntegerField()
    item_requested__pk = serializers.IntegerField()
    item_requested__name = serializers.CharField()
    item_requested__image_url = serializers.URLField()
    item_requested_quantity = serializers.IntegerField()
    created_at = serializers.DateTimeField()


class AddOfferSerializer(serializers.Serializer):
    item_offered_id = serializers.IntegerField()
    item_offered_quantity = serializers.IntegerField()
    item_requested_id = serializers.IntegerField()
    item_requested_quantity = serializers.IntegerField()


class CancelOfferSerializer(serializers.Serializer):
    #user_id = serializers.IntegerField()
    offer_id = serializers.IntegerField()
    item_offered_id = serializers.IntegerField()
    item_offered_quantity = serializers.IntegerField()


class PurchaseSerializer(serializers.Serializer):
    offer_id = serializers.IntegerField()


class UserInventorySerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    item__name = serializers.CharField()
    quantity = serializers.IntegerField()


class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'