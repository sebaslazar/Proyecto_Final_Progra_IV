from Model import ControlPlagas, ICrud, CrudModels

class ImpInterfacePlaga(ICrud.ICrud):
    
    def create(_case=2, **kwargs):
        new_control_pest = ControlPlagas.ControlPlagas(**kwargs)
        if _case == 2:
            CrudModels.CrudModels.pests.append(new_control_pest)
        return new_control_pest
    
    def data(**kwargs):            
        return CrudModels.CrudModels.pests