from trade.models import Inventory, Item, TradeOffer
from trade.serializers import PurchaseSerializer
from trade.services.utilities import item_in_inventory, enough_items, give_item_to_user, delete_offer
from django.db import transaction
from django.db.models import F




@transaction.atomic
def purchase(data: PurchaseSerializer.validated_data) -> str:
    offer = TradeOffer.objects.select_related('user', 'item').values().get(pk=data.get('offer_id'))

    #Проверяем есть ли у покупателя чем платить
    if not item_in_inventory(user_id=data.get('buyer_id'), item_id=offer.get('item_requested_id')):
        return 'buyer have no requested item'

    if not enough_items(
        user_id=data.get('buyer_id'),
        item_id=offer.get('item_requested_id'),
        quantity=offer.get('item_requested_quantity')
    ):
        return 'buyer have no requested item kurwa'

    #Забираем у покупателя requested items
    Inventory.objects.filter(
        user__pk=data.get('buyer_id'),
        item__pk=offer.get('item_requested_id')
    ).update(quantity=F('quantity') - offer.get('item_requested_quantity'))

    #Отдаем продавцу requested items
    give_item_to_user(
        user_id=data.get('seller_id'),
        item_id=offer.get('item_requested_id'),
        quantity=offer.get('item_requested_quantity')
    )

    #Отдаем покупателю offered items
    give_item_to_user(
        user_id=data.get('buyer_id'),
        item_id=offer.get('item_offered_id'),
        quantity=offer.get('item_offered_quantity')
    )

    #Удаляем Offer
    delete_offer(offer_id=data.get('offer_id'))
    return 'success'
