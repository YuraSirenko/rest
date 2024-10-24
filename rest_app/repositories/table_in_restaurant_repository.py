from rest_app.models import TableInRestaurant
from rest_app.repositories.base_repository import BaseRepository
from django.shortcuts import get_object_or_404

class CustomerRepository(BaseRepository):
    def get_all(self):
        return TableInRestaurant.objects.all()

    def get_by_id(self, id):
        return get_object_or_404(TableInRestaurant, id=id)

    def add(self, table_in_restaurant):
        table_in_restaurant.save()
        return table_in_restaurant

    def update(self, entity):
        pass

    def delete(self, id):
        pass