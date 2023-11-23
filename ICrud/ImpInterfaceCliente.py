from ICrud import ICrud
from Model import Cliente

class ImpInterfaceClient(ICrud):
    
    def create(self, **kwargs):
        return Cliente.Cliente(**kwargs)
    
    def data(self):            
        ...