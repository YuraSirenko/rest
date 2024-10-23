from rest_app.models import Order
from rest_app.repositories.base_repository import BaseRepository

class OrderRepository(BaseRepository):
    def get_all(self):
        return Order.objects.all()

    def get_by_id(self, id):
        return Order.objects.get(id=id)

    def add(self, order):
        order.save()
        return order

    def update(self, id, updated_data):
        order = self.get_by_id(id)
        for key, value in updated_data.items():
            setattr(order, key, value)
        order.save()
        return order

    def delete(self, id):
        order = self.get_by_id(id)
        order.delete()