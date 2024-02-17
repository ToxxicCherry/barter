from django.contrib.auth.models import User
from trade.models import Inventory


def get_users_inventory(user_id: int) -> dict:
    user = User.objects.get(pk=user_id)
    return user.inventory_items.values(
        'pk',
        'item__name',
        'quantity'
    )

