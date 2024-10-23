from rest_app.models import TableInRestaurant
from rest_app.repositories.base_repository import BaseRepository

class TableInRestaurantRepository(BaseRepository):
    def get_all(self):
        return TableInRestaurant.objects.all()

    def get_by_id(self, id):
        return TableInRestaurant.objects.get(id=id)

    def add(self, table):
        table.save()
        return table

    def update(self, id, updated_data):
        table = self.get_by_id(id)
        for key, value in updated_data.items():
            setattr(table, key, value)
        table.save()
        return table

    def delete(self, id):
        table = self.get_by_id(id)
        table.delete()