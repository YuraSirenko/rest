from rest_app.models import Item
from rest_app.repositories.base_repository import BaseRepository
from django.shortcuts import get_object_or_404

class ItemRepository(BaseRepository):
    def get_all(self):
        return Item.objects.all()

    def get_by_id(self, id):
        return Item.objects.get(id=id)

    def delete(self, id):
        item = self.get_by_id(id)
        item.delete()