from rest_app_2.models import ItemHasOrder
from rest_app_2.repositories.base_repository import BaseRepository
from django.shortcuts import get_object_or_404

class ItemHasOrderRepository(BaseRepository):
    def get_all(self):
        return ItemHasOrder.objects.all()

    def get_by_id(self, id):
        return ItemHasOrder.objects.get(id=id)

    def delete(self, id):
        item_has_order = self.get_by_id(id)
        item_has_order.delete()