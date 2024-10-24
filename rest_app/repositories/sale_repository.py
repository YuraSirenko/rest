from rest_app.models import Sale
from rest_app.repositories.base_repository import BaseRepository

class SaleRepository(BaseRepository):
    def get_all(self):
        return Sale.objects.all()

    def get_by_id(self, id):
        return Sale.objects.get(id=id)

    def delete(self, id):
        sale = self.get_by_id(id)
        sale.delete()