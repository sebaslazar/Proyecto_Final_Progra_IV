from abc import ABC, abstractmethod

class ICrud(ABC):
    
    @abstractmethod
    def create(self, **kwargs):
        ...
        
    @abstractmethod
    def data(self):
        ...
        
        