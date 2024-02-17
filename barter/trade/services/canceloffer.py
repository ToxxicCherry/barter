from django.db import transaction
from trade.serializers import CancelOfferSerializer
from .utilities import delete_offer, give_item_to_user


@transaction.atomic
def canceloffer(data: CancelOfferSerializer.validated_data, user_id: int) -> None:
    #Возвращаем продавцу предложенный item
    give_item_to_user(
        user_id=user_id,
        item_id=data.get('item_offered_id'),
        quantity=data.get('item_offered_quantity')
    )
    #Удаляем offer
    delete_offer(offer_id=data.get('offer_id'))