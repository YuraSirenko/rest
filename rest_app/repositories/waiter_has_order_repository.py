from rest_app.models import WaiterHasOrder
from rest_app.repositories.base_repository import BaseRepository

class WaiterHasOrderRepository(BaseRepository):
    def get_all(self):
        return WaiterHasOrder.objects.all()

    def get_by_id(self, id):
        return WaiterHasOrder.objects.get(id=id)

    def delete(self, id):
        waiter_has_order = self.get_by_id(id)
        waiter_has_order.delete()