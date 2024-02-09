from django.contrib.auth.models import User
from django.db import transaction
from .utilities import item_in_inventory, delete_offer
from trade.models import Inventory, Item
from django.db.models import F


@transaction.atomic
def canceloffer(
        user_id: int | str,
        offer_id: int | str,
        item_id: int | str,
        item_quantity: int
) -> None:
    if item_in_inventory(user_id, item_id):
        Inventory.objects.select_related('user', 'item').filter(
            user__pk=user_id,
            item__pk=item_id
        ).update(quantity=F('quantity')+item_quantity)
    else:
        Inventory.objects.create(
            user=User.objects.get(pk=user_id),
            item=Item.objects.get(pk=item_id),
            quantity=item_quantity
        )
    delete_offer(offer_id=offer_id)