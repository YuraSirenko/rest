from rest_app_2.models import Sale
from rest_app_2.repositories.base_repository import BaseRepository

class SaleRepository(BaseRepository):
    def get_all(self):
        return Sale.objects.all()

    def get_by_id(self, id):
        return Sale.objects.get(id=id)

    def delete(self, id):
        sale = self.get_by_id(id)
        sale.delete()

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