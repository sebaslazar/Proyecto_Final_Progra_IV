from abc import ABC, abstractmethod

class ICrud(ABC):
    
    @abstractmethod
    def create(**kwargs):
        raise NotImplementedError

    @abstractmethod
    def search(**kwargs):
        raise NotImplementedError
        
    @abstractmethod
    def data(**kwargs):
        raise NotImplementedError
        
        