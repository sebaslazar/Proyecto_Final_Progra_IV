from Model import Factura, CrudModels, ICrud

class ImpInterfaceFactura(ICrud.ICrud):
    
    def create(**kwargs):
        return Factura.Factura(**kwargs)
    
    def append_products(**kwargs):
        bill = kwargs["bill"]
        for product in kwargs["products"]:
            bill.products = product
    
    def search(**kwargs):
        for bill in CrudModels.CrudModels.clients:
            print(vars(bill))
            if vars(bill) == kwargs:
                return bill
            
        return False
    
    def data(self):            
        ...