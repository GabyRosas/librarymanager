from abc import ABC, abstractmethod  # ABC una clase base para definir clases abstractas


# y  abstractmethod decorador que se usa para definir métodos abstractos

class InterfaceModel(ABC):
    @abstractmethod
    def create(self, data):  # data es una paranetro para crear nueva data en BBDD
        pass

    @abstractmethod
    def read(self, criteria=None):  # criteria como un filtro para buscar con parametros espicificos
        pass

    @abstractmethod
    def update(self, data, criteria=None):
        pass

    @abstractmethod
    def delete(self, criteria=None):
        pass
