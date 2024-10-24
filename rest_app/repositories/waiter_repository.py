from rest_app.models import Waiter
from rest_app.repositories.base_repository import BaseRepository
from django.shortcuts import get_object_or_404

class WaiterRepository(BaseRepository):
    def get_all(self):
        return Waiter.objects.all()

    def get_by_id(self, id):
        return get_object_or_404(Waiter, id=id)

    def add(self, waiter):
        waiter.save()
        return waiter

    def update(self, entity):
        pass

    def delete(self, id):
        pass