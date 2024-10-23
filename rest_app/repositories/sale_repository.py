from rest_app.models import Sale
from rest_app.repositories.base_repository import BaseRepository
from django.shortcuts import get_object_or_404

class SaleRepository(BaseRepository):
    def get_all(self):
        return Sale.objects.all()

    def get_by_id(self, id):
        return get_object_or_404(Sale, id=id)

    def add(self, sale):
        sale.save()

    def update(self, entity):
        pass

    def delete(self, id):
        pass