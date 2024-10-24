from rest_app.models import Order
from rest_app.repositories.base_repository import BaseRepository

class OrderRepository(BaseRepository):
    def get_all(self):
        return Order.objects.all()

    def get_by_id(self, id):
        return Order.objects.get(id=id)

    def delete(self, id):
        order = self.get_by_id(id)
        order.delete()