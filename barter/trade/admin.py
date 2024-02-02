from django.contrib import admin
from trade.models import *

admin.site.register(Item)
admin.site.register(Inventory)
admin.site.register(InventoryItem)
admin.site.register(TradeOffer)

