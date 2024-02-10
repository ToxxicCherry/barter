from django.db import transaction
from .utilities import delete_offer, give_item_to_user


@transaction.atomic
def canceloffer(
        user_id: int | str,
        offer_id: int | str,
        item_id: int | str,
        item_quantity: int
) -> None:
    #Возвращаем продавцу предложенный item
    give_item_to_user(user_id=user_id, item_id=item_id, quantity=item_quantity)
    #Удаляем offer
    delete_offer(offer_id=offer_id)