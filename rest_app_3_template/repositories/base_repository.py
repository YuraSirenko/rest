from abc import ABC, abstractmethod

class BaseRepository(ABC):
    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_id(self, id):
        pass

    @abstractmethod
    def delete(self, id):
        pass

    @abstractmethod
    def create(self,**kwargs):
        pass

    @abstractmethod
    def update(self, id,**kwargs):
        pass