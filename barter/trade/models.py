from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Название предмета")
    description = models.TextField(blank=True, null=True, verbose_name="Описание предмета")
    image_url = models.URLField(blank=True, null=True, verbose_name="Ссылка на изображение")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Предмет"
        verbose_name_plural = "Предметы"


class Inventory(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    items = models.ManyToManyField('Item', related_name='inventories', through='InventoryItem', verbose_name="Предметы в инвентаре")

    def __str__(self):
        return f"Inventar of {self.user.username}"

    class Meta:
        verbose_name = "Инвентарь"
        verbose_name_plural = "Инвентари"


class InventoryItem(models.Model):
    inventory = models.ForeignKey('Inventory', on_delete=models.CASCADE, verbose_name="Инвентарь")
    item = models.ForeignKey('Item', on_delete=models.CASCADE, verbose_name="Предмет")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Количество")

    def __str__(self):
        return f"{self.item.name} in {self.inventory.user.username}'s inventory"

    class Meta:
        verbose_name = "Элемент инвентаря"
        verbose_name_plural = "Элементы инвентаря"


class TradeOffer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    title = models.CharField(max_length=255, verbose_name="Заголовок предложения")
    description = models.TextField(verbose_name="Описание предложения")
    items_offered = models.ManyToManyField('Item', related_name='trade_offers_offered', verbose_name="Предлагаемые предметы")
    items_offered_quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')
    items_requested = models.ManyToManyField('Item', related_name='trade_offers_requested', verbose_name="Желаемые предметы")
    items_requested_quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"Предложение обмена от {self.user.username}: {self.title}"

    class Meta:
        verbose_name = "Предложение обмена"
        verbose_name_plural = "Предложения обмена"