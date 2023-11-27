from Model import ControlFertilizantes, ICrud, CrudModels

class ImpInterfaceFertilizantes(ICrud.ICrud):
    
    def create(_case=2, **kwargs):
        new_fertilizer = ControlFertilizantes.ControlFertilizantes(**kwargs)
        if _case == 2:
            CrudModels.CrudModels.fertilizers.append(new_fertilizer)
        return new_fertilizer
    
    def data(**kwargs):            
        return CrudModels.CrudModels.fertilizers