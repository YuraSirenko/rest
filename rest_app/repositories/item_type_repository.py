from rest_app.models import ItemType
from rest_app.repositories.base_repository import BaseRepository
from django.shortcuts import get_object_or_404

class CustomerRepository(BaseRepository):
    def get_all(self):
        return ItemType.objects.all()

    def get_by_id(self, id):
        return get_object_or_404(ItemType, id=id)

    def add(self, item_type):
        item_type.save()
        return item_type

    def update(self, entity):
        pass

    def delete(self, id):
        pass