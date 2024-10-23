from rest_app.models import Customer
from rest_app.repositories.base_repository import BaseRepository

class CustomerRepository(BaseRepository):
    def get_all(self):
        return Customer.objects.all()

    def get_by_id(self, id):
        return Customer.objects.get(id=id)

    def add(self, customer):
        customer.save()
        return customer

    def update(self, id, updated_data):
        customer = self.get_by_id(id)
        for key, value in updated_data.items():
            setattr(customer, key, value)
        customer.save()
        return customer

    def delete(self, id):
        customer = self.get_by_id(id)
        customer.delete()