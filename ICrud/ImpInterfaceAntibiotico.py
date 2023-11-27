from Model import Antibioticos, ICrud, CrudModels

class ImpInterfaceAntibiotico(ICrud.ICrud):
    
    def create(_case=2, **kwargs):
        new_antibiotic = Antibioticos.Antibioticos(**kwargs)
        if _case == 2:
            CrudModels.CrudModels.antibiotics.append(new_antibiotic)
        return new_antibiotic
    
    
    def data(**kwargs):            
        return CrudModels.CrudModels.antibiotics