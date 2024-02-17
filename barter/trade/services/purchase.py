from trade.models import Inventory, Item, TradeOffer
from trade.serializers import PurchaseSerializer
from trade.services.utilities import \
    item_in_inventory, \
    enough_items, \
    give_item_to_user, \
    delete_offer, \
    take_away_item_from_user
from django.db import transaction



@transaction.atomic
def purchase(data: PurchaseSerializer.validated_data, buyer_id: int) -> str:
    offer = TradeOffer.objects.select_related('user', 'item').values().get(pk=data.get('offer_id'))

    #Проверяем есть ли у покупателя чем платить
    if not item_in_inventory(user_id=buyer_id, item_id=offer.get('item_requested_id')):
        return 'the user does not have enough funds'

    if not enough_items(
        user_id=buyer_id,
        item_id=offer.get('item_requested_id'),
        quantity=offer.get('item_requested_quantity')
    ):
        return 'the user does not have enough funds'

    #Забираем у покупателя requested items
    take_away_item_from_user(
        user_id=buyer_id,
        item_id=offer.get('item_requested_id'),
        quantity=offer.get('item_requested_quantity'))

    #Отдаем продавцу requested items
    give_item_to_user(
        user_id=offer.get('user_id'),
        item_id=offer.get('item_requested_id'),
        quantity=offer.get('item_requested_quantity')
    )

    #Отдаем покупателю offered items
    give_item_to_user(
        user_id=buyer_id,
        item_id=offer.get('item_offered_id'),
        quantity=offer.get('item_offered_quantity')
    )

    #Удаляем Offer
    delete_offer(offer_id=data.get('offer_id'))
    return 'success'
