from rest_app.models import PaymentMethod
from rest_app.repositories.base_repository import BaseRepository

class PaymentMethodRepository(BaseRepository):
    def get_all(self):
        return PaymentMethod.objects.all()

    def get_by_id(self, id):
        return PaymentMethod.objects.get(id=id)

    def add(self, payment_method):
        payment_method.save()
        return payment_method

    def update(self, id, updated_data):
        payment_method = self.get_by_id(id)
        for key, value in updated_data.items():
            setattr(payment_method, key, value)
        payment_method.save()
        return payment_method

    def delete(self, id):
        payment_method = self.get_by_id(id)
        payment_method.delete()