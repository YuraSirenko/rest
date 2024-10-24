from rest_app.models import Item
from rest_app.repositories.base_repository import BaseRepository
from django.shortcuts import get_object_or_404

class CustomerRepository(BaseRepository):
    def get_all(self):
        return Item.objects.all()

    def get_by_id(self, id):
        return get_object_or_404(Item, id=id)

    def add(self, item):
        item.save()
        return item

    def update(self, entity):
        pass

    def delete(self, id):
        pass