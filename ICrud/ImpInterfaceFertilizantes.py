from ICrud import ICrud
from Model import ControlFertilizantes

class ImpInterfaceFertilizantes(ICrud):
    
    def create(self, **kwargs):
        return ControlFertilizantes.ControlFertilizantes(**kwargs)
    
    def data(self):            
        ...