from rest_app.models import SalaryType
from rest_app.repositories.base_repository import BaseRepository

class SalaryTypeRepository(BaseRepository):
    def get_all(self):
        return SalaryType.objects.all()

    def get_by_id(self, id):
        return SalaryType.objects.get(id=id)

    def delete(self, id):
        salary_type = self.get_by_id(id)
        salary_type.delete()