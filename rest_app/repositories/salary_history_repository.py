from rest_app.models import SalaryHistory
from rest_app.repositories.base_repository import BaseRepository

class SalaryHistoryRepository(BaseRepository):
    def get_all(self):
        return SalaryHistory.objects.all()

    def get_by_id(self, id):
        return SalaryHistory.objects.get(id=id)

    def delete(self, id):
        salary_history = self.get_by_id(id)
        salary_history.delete()