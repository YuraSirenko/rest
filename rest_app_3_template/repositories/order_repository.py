from rest_app_2.models import Order
from .base_repository import BaseRepository
from datetime import datetime

class OrderRepository(BaseRepository):
    def get_all(self):
        return Order.objects.all()

    def get_by_id(self, id):
        return Order.objects.get(id=id)

    def delete(self, id):
        order = self.get_by_id(id)
        order.delete()

    def create(self, table_id, customer_id, number_of_customers, payment_method, total_sum, event_started, event_ended):
        order = Order(
            table_id=table_id,
            customer_id=customer_id,
            number_of_customers=number_of_customers,
            payment_method=payment_method,
            total_sum=total_sum or 0.00,
            event_started=event_started or datetime.now(),
            event_ended=event_ended
        )
        order.save()
        return order

    def update(self, id, **kwargs):
        order = self.get_by_id(id)
        for key, value in kwargs.items():
            setattr(order, key, value)
        order.save()
        return order