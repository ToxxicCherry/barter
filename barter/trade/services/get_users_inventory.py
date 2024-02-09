from django.contrib.auth.models import User
from trade.models import Inventory


def get_users_inventory(user_id: int) -> dict:
    user = {'items': Inventory.objects.filter(user__id=user_id).values(
        'item__pk',
        'quantity'
    ),
        'user_id': user_id}
    user.update(User.objects.values('username').get(pk=user_id))
    return user
