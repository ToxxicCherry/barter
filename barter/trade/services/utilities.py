from django.contrib.auth.models import User
from django.db.models import F

from trade.models import Inventory, TradeOffer, Item
from django.db import models


# def delete_item_from_users_inv(
#         user_id: int | str,
#         item_id: int | str
# ) -> None:
#
#     Inventory.objects.filter(
#         user__pk=user_id,
#         item__pk=item_id
#     ).delete()


def delete_offer(offer_id: int | str) -> None:
    TradeOffer.objects.filter(pk=offer_id).delete()


# def item_in_inventory(
#         user_id: int | str,
#         item_id: int | str
# ) -> bool:
#     try:
#         Inventory.objects.select_related('item', 'user').get(user__pk=user_id, item__pk=item_id)
#         return True
#     except models.ObjectDoesNotExist:
#         return False


def enough_items(
        user_id: int | str,
        item_id: int | str,
        quantity: int
) -> bool:

    obj, created = Inventory.objects.values('quantity').get_or_create(
        user=User.objects.get(pk=user_id),
        item=Item.objects.get(pk=item_id)
    )

    return False if created else quantity <= obj.get('quantity')


def give_item_to_user(
        user_id: int | str,
        item_id: int | str,
        quantity: int
) -> None:
    obj, created = Inventory.objects.get_or_create(
        user=User.objects.get(pk=user_id),
        item=Item.objects.get(pk=item_id)
    )
    if created:
        obj.quantity = quantity
    else:
        #obj.quantity = F('quantity') + quantity
        obj.quantity += quantity
    obj.save()


def take_away_item_from_user(
        user_id: int | str,
        item_id: int | str,
        quantity: int
) -> None:

    obj = Inventory.objects.get(
        user__pk=user_id,
        item__pk=item_id,
    )
    #obj.quantity = F('quantity') - quantity
    obj.quantity -= quantity
    obj.save()









