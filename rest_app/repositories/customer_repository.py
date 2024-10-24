from rest_app.models import Customer
from rest_app.repositories.base_repository import BaseRepository
from django.shortcuts import get_object_or_404

class CustomerRepository(BaseRepository):
    def get_all(self):
        return Customer.objects.all()

    def get_by_id(self, id):
        return get_object_or_404(Customer, id=id)

    def add(self, customer):
        customer.save()
        return customer

    def update(self, entity):
        pass

    def delete(self, id):
        pass