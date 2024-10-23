from rest_app.models import Sale
from rest_app.repositories.base_repository import BaseRepository

class SaleRepository(BaseRepository):
    def get_all(self):
        return Sale.objects.all()

    def get_by_id(self, id):
        return Sale.objects.get(id=id)

    def add(self, sale):
        sale.save()
        return sale

    def update(self, id, updated_data):
        sale = self.get_by_id(id)
        for key, value in updated_data.items():
            setattr(sale, key, value)
        sale.save()
        return sale

    def delete(self, id):
        sale = self.get_by_id(id)
        sale.delete()