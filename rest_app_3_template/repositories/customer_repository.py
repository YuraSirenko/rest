from rest_app_2.models import Customer
from rest_app_2.repositories.base_repository import BaseRepository

class CustomerRepository(BaseRepository):
    def get_all(self):
        return Customer.objects.all()

    def get_by_id(self, id):
        return Customer.objects.get(id=id)

    def delete(self, id):
        customer = self.get_by_id(id)
        customer.delete()


    def create(self, **kwargs):
        customer = Customer(**kwargs)
        customer.save()
        return customer

    def update(self, id, **kwargs):
        customer = self.get_by_id(id)
        for key, value in kwargs.items():
            setattr(customer, key, value)
        customer.save()
        return customer