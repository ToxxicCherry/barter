from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from trade.models import TradeOffer, Item, Inventory
from django.contrib.auth.models import User


class TradeOffersTests(APITestCase):
    def setUp(self) -> None:
        User.objects.create_user(username='Happy')

        Item.objects.create(name='Chaos orb')
        Item.objects.create(name='Exalted orb')
        Item.objects.create(name='Divine orb')

        Inventory.objects.create(
            user=User.objects.get(username='Happy'),
            item=Item.objects.get(name='Chaos orb'),
            quantity=1000
        )
        Inventory.objects.create(
            user=User.objects.get(username='Happy'),
            item=Item.objects.get(name='Exalted orb'),
            quantity=100
        )
        Inventory.objects.create(
            user=User.objects.get(username='Happy'),
            item=Item.objects.get(name='Exalted orb'),
            quantity=10
        )
        TradeOffer.objects.create(
            user=User.objects.get(username='Happy'),
            item_offered=Item.objects.get(name='Chaos orb'),
            item_offered_quantity=10,
            item_requested=Item.objects.get(name='Divine orb'),
            item_requested_quantity=1
        )

    def test_offers_list(self):
        response = self.client.get(reverse('offerslist'))
        print(response.data.get('offers'))
        #self.assertEquals(response.status_code, status.HTTP_200_OK)
