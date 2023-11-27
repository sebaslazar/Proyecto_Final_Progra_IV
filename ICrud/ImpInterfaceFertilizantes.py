from Model import ControlFertilizantes, ICrud

class ImpInterfaceFertilizantes(ICrud.ICrud):
    
    def create(**kwargs):
        return ControlFertilizantes.ControlFertilizantes(**kwargs)
    
    def data(self):            
        ...