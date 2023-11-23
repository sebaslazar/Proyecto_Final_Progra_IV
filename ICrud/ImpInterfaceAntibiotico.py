from Model import Antibioticos
from ICrud import ICrud

class ImpInterfaceAntibiotico(ICrud):
    
    def create(self, **kwargs):
        return Antibioticos.Antibioticos(**kwargs)
    
    def data(self):            
        ...