from rest_app.models import Order
from rest_app.repositories.base_repository import BaseRepository
from django.shortcuts import get_object_or_404

class OrderRepository(BaseRepository):
    def get_all(self):
        return Order.objects.all()

    def get_by_id(self, id):
        return get_object_or_404(Order, id=id)

    def add(self, order):
        order.save()
        return order

    def update(self, entity):
        pass

    def delete(self, id):
        pass