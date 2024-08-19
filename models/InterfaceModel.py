from abc import ABC, abstractmethod

class InterfaceModel(ABC):
    @abstractmethod
    def create(self, data):
        pass

    @abstractmethod
    def read(self, criteria=None):
        pass

    @abstractmethod
    def update(self, data, criteria=None):
        pass

    @abstractmethod
    def delete(self, criteria=None):
        pass
