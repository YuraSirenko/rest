from rest_app.models import PaymentMethod
from rest_app.repositories.base_repository import BaseRepository
from django.shortcuts import get_object_or_404

class PaymentMethodRepository(BaseRepository):
    def get_all(self):
        return PaymentMethod.objects.all()

    def get_by_id(self, id):
        return get_object_or_404(PaymentMethod, id=id)

    def add(self, payment_method):
        payment_method.save()
        return payment_method

    def update(self, entity):
        pass

    def delete(self, id):
        pass