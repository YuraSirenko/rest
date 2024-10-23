from rest_app.models import ItemType
from rest_app.repositories.base_repository import BaseRepository
from django.shortcuts import get_object_or_404

class ItemTypeRepository(BaseRepository):
    def get_all(self):
        return ItemType.objects.all()

    def get_by_id(self, id):
        return ItemType.objects.get(id=id)

    def add(self, item_type):
        item_type.save()
        return item_type

    def update(self, id, updated_data):
        item_type = self.get_by_id(id)
        for key, value in updated_data.items():
            setattr(item_type, key, value)
        item_type.save()
        return item_type

    def delete(self, id):
        item_type = self.get_by_id(id)
        item_type.delete()