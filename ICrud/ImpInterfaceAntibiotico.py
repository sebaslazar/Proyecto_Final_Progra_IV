from Model import Antibioticos, ICrud

class ImpInterfaceAntibiotico(ICrud.ICrud):
    
    def create(**kwargs):
        return Antibioticos.Antibioticos(**kwargs)
    
    def search(**kwargs):
        ...
    
    def data(self):            
        ...