from ICrud.ImpInterfaceFactura import ImpInterfaceFactura

class BillControler:
    
    @staticmethod
    def create(**kwargs):
        return ImpInterfaceFactura.create(**kwargs)
    
    @staticmethod
    def append_product(**kwargs):
        ImpInterfaceFactura.append_products(**kwargs)
    
    @staticmethod
    def search(**kwargs):
        return ImpInterfaceFactura