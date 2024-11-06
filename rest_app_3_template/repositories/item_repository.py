from rest_app_2.models import Item
from rest_app_2.repositories.base_repository import BaseRepository
from django.shortcuts import get_object_or_404

class ItemRepository(BaseRepository):
    def get_all(self):
        return Item.objects.all()

    def get_by_id(self, id):
        return Item.objects.get(id=id)

    def delete(self, id):
        item = self.get_by_id(id)
        item.delete()

    def create(self, **kwargs):
        waiter_has_order = WaiterHasOrder(**kwargs)
        waiter_has_order.save()
        return waiter_has_order

    def update(self, id, **kwargs):
        waiter_has_order = self.get_by_id(id)
        for key, value in kwargs.items():
            setattr(waiter_has_order, key, value)
        waiter_has_order.save()
        return waiter_has_order