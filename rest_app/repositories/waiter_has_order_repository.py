from rest_app.models import WaiterHasOrder
from rest_app.repositories.base_repository import BaseRepository
from django.shortcuts import get_object_or_404

class CustomerRepository(BaseRepository):
    def get_all(self):
        return WaiterHasOrder.objects.all()

    def get_by_id(self, id):
        return get_object_or_404(WaiterHasOrder, id=id)

    def add(self, waiter_has_order):
        waiter_has_order.save()
        return waiter_has_order

    def update(self, entity):
        pass

    def delete(self, id):
        pass