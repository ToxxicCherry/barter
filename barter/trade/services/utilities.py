from django.contrib.auth.models import User
from trade.models import Inventory, TradeOffer, Item
from django.db import models



def delete_item_from_users_inv(user_id: int | str, item_id: int | str) -> None:
    Inventory.objects.filter(
        user__pk=user_id,
        item__pk=item_id
    ).delete()


def add_new_item_to_user_inventory(
        user_id: int | str,
        item_id: int | str,
        quantity: int | str,
) -> None:

    Inventory.objects.select_related('Item').create(
        user=User.objects.get(pk=user_id),
        item__pk=Item.objects.get(pk=item_id),
        quantity=quantity
    )


def delete_offer(offer_id: int | str) -> None:
    TradeOffer.objects.filter(pk=offer_id).delete()


def item_in_inventory(
        user_id: int | str,
        item_id: int | str
) -> bool:
    try:
        Inventory.objects.select_related('item', 'user').get(user__pk=user_id, item__pk=item_id)
        return True
    except models.ObjectDoesNotExist:
        return False











