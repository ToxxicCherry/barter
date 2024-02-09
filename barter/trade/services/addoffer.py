from django.contrib.auth.models import User
from django.db import transaction
from .utilities import delete_item_from_users_inv
from trade.models import Item, Inventory, TradeOffer


@transaction.atomic
def addoffer(data: dict) -> dict:
    users_offered_item_quantity = Inventory.objects.values('quantity').get(
        user__pk=data.get('user_id'),
        item__pk=data.get('item_offered_id')
    )

    difference = int(users_offered_item_quantity.get('quantity')) - int(data.get('item_offered_quantity'))
    if difference < 0:
        return {'status': 'error: not enough quantity'}

    if difference == 0:
        delete_item_from_users_inv(data.get('user_id'), data.get('item_offered_id'))
    else:
        Inventory.objects.filter(
            user__pk=data.get('user_id'),
            item__pk=data.get('item_offered_id')
        ).update(quantity=difference)

    TradeOffer.objects.select_related('Item').create(
        user=User.objects.get(pk=data.get('user_id')),
        item_offered=Item.objects.get(pk=data.get('item_offered_id')),
        item_offered_quantity=data.get('item_offered_quantity'),
        item_requested=Item.objects.get(pk=data.get('item_requested_id')),
        item_requested_quantity=data.get('item_requested_quantity')
    )

    return {'status': 'offer added'}


