from ICrud import ICrud
from Model import Factura

class ImpInterfaceFactura(ICrud):
    
    def create(self, **kwargs):
        return Factura.Factura(**kwargs)
    
    def data(self):            
        ...