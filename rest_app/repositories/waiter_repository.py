from rest_app.models import Waiter
from rest_app.repositories.base_repository import BaseRepository

class WaiterRepository(BaseRepository):
    def get_all(self):
        return Waiter.objects.all()

    def get_by_id(self, id):
        return Waiter.objects.get(id=id)

    def add(self, waiter):
        waiter.save()
        return waiter

    def update(self, id, updated_data):
        waiter = self.get_by_id(id)
        for key, value in updated_data.items():
            setattr(waiter, key, value)
        waiter.save()
        return waiter

    def delete(self, id):
        waiter = self.get_by_id(id)
        waiter.delete()