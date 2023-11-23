from ICrud.ImpInterfaceFactura import ImpInterfaceFactura

class BillControler:
    
    @staticmethod
    def create(**kwargs):
        ImpInterfaceFactura.create(**kwargs)
        
    @staticmethod
    def search(**kwargs):
        return ImpInterfaceFactura