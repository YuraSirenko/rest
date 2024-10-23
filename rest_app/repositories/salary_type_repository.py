from rest_app.models import SalaryType
from rest_app.repositories.base_repository import BaseRepository
from django.shortcuts import get_object_or_404

class SalaryTypeRepository(BaseRepository):
    def get_all(self):
        return SalaryType.objects.all()

    def get_by_id(self, id):
        return get_object_or_404(SalaryType, id=id)

    def add(self, salary_type):
        salary_type.save()

    def update(self, entity):
        pass

    def delete(self, id):
        pass