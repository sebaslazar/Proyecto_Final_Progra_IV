from ICrud import ICrud
from Model import Factura, CrudModels

class ImpInterfaceFactura(ICrud):
    
    def create(self, **kwargs):
        return Factura.Factura(**kwargs)
    
    def search(self, **kwargs):
        for bill in CrudModels.CrudModels.clients:
            print(vars(bill))
            if vars(bill) == kwargs:
                return bill
            
        return False
    
    def data(self):            
        ...