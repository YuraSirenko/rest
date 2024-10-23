from abc import ABC, abstractmethod

class BaseRepository(ABC):
    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_id(self, id):
        pass

    @abstractmethod
    def add(self, entity):
        pass

    @abstractmethod
    def update(self, id, updated_data):
        pass

    @abstractmethod
    def delete(self, id):
        pass