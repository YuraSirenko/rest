from rest_app_2.models import ItemType
from rest_app_2.repositories.base_repository import BaseRepository
from django.shortcuts import get_object_or_404

class ItemTypeRepository(BaseRepository):
    def get_all(self):
        return ItemType.objects.all()

    def get_by_id(self, id):
        return ItemType.objects.get(id=id)

    def delete(self, id):
        item_type = self.get_by_id(id)
        item_type.delete()

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