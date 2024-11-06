from rest_app_2.models import PaymentMethod
from rest_app_2.repositories.base_repository import BaseRepository

class PaymentMethodRepository(BaseRepository):
    def get_all(self):
        return PaymentMethod.objects.all()

    def get_by_id(self, id):
        return PaymentMethod.objects.get(id=id)


    def delete(self, id):
        payment_method = self.get_by_id(id)
        payment_method.delete()