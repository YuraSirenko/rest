from rest_app.models import SalaryType
from rest_app.repositories.base_repository import BaseRepository

class SalaryTypeRepository(BaseRepository):
    def get_all(self):
        return SalaryType.objects.all()

    def get_by_id(self, id):
        return SalaryType.objects.get(id=id)

    def add(self, salary_type):
        salary_type.save()
        return salary_type

    def update(self, id, updated_data):
        salary_type = self.get_by_id(id)
        for key, value in updated_data.items():
            setattr(salary_type, key, value)
        salary_type.save()
        return salary_type

    def delete(self, id):
        salary_type = self.get_by_id(id)
        salary_type.delete()