from abc import ABC, abstractmethod

class ICrud(ABC):
    
    @abstractmethod
    def create(self, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def search(self, **kwargs):
        raise NotImplementedError
        
    @abstractmethod
    def data(self):
        raise NotImplementedError
        
        