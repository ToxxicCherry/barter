from django.contrib.auth.models import User
from django.db import transaction
from trade.models import Item, Inventory, TradeOffer
from trade.services.utilities import enough_items


@transaction.atomic
def addoffer(data: dict, user_id: int) -> dict:
    users_offered_item_quantity = Inventory.objects.values('quantity').get(
        user__pk=user_id,
        item__pk=data.get('item_offered_id')
    )

    difference = int(users_offered_item_quantity.get('quantity')) - int(data.get('item_offered_quantity'))
    if difference < 0:
        return {'status': 'error: not enough quantity'}

    Inventory.objects.filter(
        user_id=user_id,
        item_id=data.get('item_offered_id')
    ).update(quantity=difference)

    TradeOffer.objects.create(
        user=User.objects.get(pk=user_id),
        item_offered=Item.objects.get(pk=data.get('item_offered_id')),
        item_offered_quantity=data.get('item_offered_quantity'),
        item_requested=Item.objects.get(pk=data.get('item_requested_id')),
        item_requested_quantity=data.get('item_requested_quantity')
    )

    return {'status': 'offer added'}


