from rest_app_2.models import TableInRestaurant
from rest_app_2.repositories.base_repository import BaseRepository

class TableInRestaurantRepository(BaseRepository):
    def get_all(self):
        return TableInRestaurant.objects.all()

    def get_by_id(self, id):
        return TableInRestaurant.objects.get(id=id)

    def delete(self, id):
        table = self.get_by_id(id)
        table.delete()

    def create_waiter_has_order(self, **kwargs):
        waiter_has_order = WaiterHasOrder(**kwargs)
        waiter_has_order.save()
        return waiter_has_order

    def update_waiter_has_order(self, id, **kwargs):
        waiter_has_order = self.get_by_id(id)
        for key, value in kwargs.items():
            setattr(waiter_has_order, key, value)
        waiter_has_order.save()
        return waiter_has_order