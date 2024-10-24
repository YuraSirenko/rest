from rest_app.models import SalaryHistory
from rest_app.repositories.base_repository import BaseRepository
from django.shortcuts import get_object_or_404

class CustomerRepository(BaseRepository):
    def get_all(self):
        return SalaryHistory.objects.all()

    def get_by_id(self, id):
        return get_object_or_404(SalaryHistory, id=id)

    def add(self, salary_history):
        salary_history.save()
        return salary_history

    def update(self, entity):
        pass

    def delete(self, id):
        pass