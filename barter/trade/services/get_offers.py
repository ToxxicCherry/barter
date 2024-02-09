from django.db.models.query import QuerySet
from trade.models import TradeOffer


def get_offers() -> QuerySet:
    return TradeOffer.objects.select_related('User', 'Item').values(
            'pk',
            'user__pk',
            'user__username',
            'item_offered__pk',
            'item_offered__name',
            'item_offered__description',
            'item_offered__image_url',
            'item_offered_quantity',
            'item_requested__pk',
            'item_requested__name',
            'item_requested__image_url',
            'item_requested_quantity',
            'created_at'
        )