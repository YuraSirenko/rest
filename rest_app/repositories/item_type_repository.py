from rest_app.models import ItemType
from rest_app.repositories.base_repository import BaseRepository
from django.shortcuts import get_object_or_404

class ItemTypeRepository(BaseRepository):
    def get_all(self):
        return ItemType.objects.all()

    def get_by_id(self, id):
        return ItemType.objects.get(id=id)

    def delete(self, id):
        item_type = self.get_by_id(id)
        item_type.delete()