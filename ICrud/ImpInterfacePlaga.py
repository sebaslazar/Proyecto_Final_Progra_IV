from Model import ControlPlagas
from ICrud import ICrud

class ImpInterfacePlaga(ICrud):
    
    def create(self, **kwargs):
        return ControlPlagas.ControlPlagas(**kwargs)
    
    def data(self):            
        ...