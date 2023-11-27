from Model import ControlPlagas, ICrud

class ImpInterfacePlaga(ICrud.ICrud):
    
    def create(**kwargs):
        return ControlPlagas.ControlPlagas(**kwargs)
    
    def data(**kwargs):            
        ...