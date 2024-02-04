from rest_framework import serializers


class TradeOffersSerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    user__pk = serializers.IntegerField()
    user__username = serializers.CharField()
    title = serializers.CharField()
    description = serializers.CharField()
    items_offered__pk = serializers.IntegerField()
    items_offered__name = serializers.CharField()
    items_offered__description = serializers.CharField()
    items_offered_quantity = serializers.IntegerField()
    items_requested__pk = serializers.IntegerField()
    items_requested__name = serializers.CharField()
    items_requested_quantity = serializers.IntegerField()
    created_at = serializers.DateTimeField()