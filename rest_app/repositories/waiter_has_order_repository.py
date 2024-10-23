from rest_app.models import WaiterHasOrder
from rest_app.repositories.base_repository import BaseRepository

class WaiterHasOrderRepository(BaseRepository):
    def get_all(self):
        return WaiterHasOrder.objects.all()

    def get_by_id(self, id):
        return WaiterHasOrder.objects.get(id=id)

    def add(self, waiter_has_order):
        waiter_has_order.save()
        return waiter_has_order

    def update(self, id, updated_data):
        waiter_has_order = self.get_by_id(id)
        for key, value in updated_data.items():
            setattr(waiter_has_order, key, value)
        waiter_has_order.save()
        return waiter_has_order

    def delete(self, id):
        waiter_has_order = self.get_by_id(id)
        waiter_has_order.delete()