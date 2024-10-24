from rest_app.models import TableInRestaurant
from rest_app.repositories.base_repository import BaseRepository

class TableInRestaurantRepository(BaseRepository):
    def get_all(self):
        return TableInRestaurant.objects.all()

    def get_by_id(self, id):
        return TableInRestaurant.objects.get(id=id)

    def delete(self, id):
        table = self.get_by_id(id)
        table.delete()