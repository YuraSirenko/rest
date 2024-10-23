from rest_app.models import ItemHasOrder
from rest_app.repositories.base_repository import BaseRepository
from django.shortcuts import get_object_or_404

class CustomerRepository(BaseRepository):
    def get_all(self):
        return ItemHasOrder.objects.all()

    def get_by_id(self, id):
        return get_object_or_404(ItemHasOrder, id=id)

    def add(self, item_has_order):
        item_has_order.save()
        return item_has_order

    def update(self, entity):
        pass

    def delete(self, id):
        pass